# -*- coding: utf-8 -*-
"""
Adaptive Mistake Analysis & Dynamic Remedial Drill Generator
Supports English (QWERTY) and all 13 Indian Scripts (InScript).
"""

from curriculum_en import FINGER_LABELS, get_finger_map_for_language
from curriculum_inscript import INDIAN_LANGUAGE_PACKS

WORD_BANK_BY_CHAR = {
    "a": ["add", "ask", "all", "adapt", "area", "data", "plaza", "alpha", "salad", "balance"],
    "b": ["back", "best", "bold", "bright", "bubble", "number", "combine", "habit", "global", "orbit"],
    "c": ["clear", "check", "choice", "cycle", "classic", "success", "science", "accurate", "focus", "practice"],
    "d": ["dad", "data", "deep", "decide", "divide", "modern", "steady", "standard", "ladder", "hidden"],
    "e": ["each", "even", "exact", "energy", "element", "level", "better", "letter", "complete", "excellence"],
    "f": ["fast", "find", "focus", "first", "future", "office", "effort", "effect", "buffer", "fluent"],
    "g": ["good", "great", "group", "guide", "global", "logic", "target", "signal", "progress", "engage"],
    "h": ["half", "high", "habit", "health", "history", "thought", "through", "rhythm", "method", "anchor"],
    "i": ["idea", "input", "index", "inside", "insight", "limit", "visit", "finish", "spirit", "digital"],
    "j": ["join", "jump", "just", "judge", "journal", "project", "object", "subject", "adjust", "major"],
    "k": ["keep", "key", "kind", "know", "kernel", "market", "packet", "skill", "spark", "check"],
    "l": ["lead", "learn", "level", "light", "logic", "local", "parallel", "skillful", "global", "install"],
    "m": ["make", "main", "memory", "method", "modern", "moment", "system", "common", "maximum", "minimum"],
    "n": ["name", "near", "next", "number", "nature", "network", "pattern", "connect", "instant", "balance"],
    "o": ["open", "order", "option", "object", "output", "follow", "control", "smooth", "motion", "protocol"],
    "p": ["pace", "page", "power", "proper", "purpose", "people", "prepare", "support", "pattern", "applied"],
    "q": ["quick", "quiet", "quite", "quote", "quality", "quarter", "query", "request", "require", "equal"],
    "r": ["rate", "reach", "ready", "record", "result", "return", "mirror", "error", "correct", "program"],
    "s": ["safe", "same", "score", "sense", "system", "series", "success", "session", "process", "assist"],
    "t": ["take", "task", "test", "time", "target", "total", "letter", "matter", "pattern", "station"],
    "u": ["unit", "user", "until", "update", "useful", "future", "nature", "result", "support", "structure"],
    "v": ["value", "valid", "view", "voice", "vital", "active", "level", "native", "service", "improve"],
    "w": ["wait", "walk", "water", "watch", "world", "window", "network", "forward", "power", "answer"],
    "x": ["exact", "exam", "exist", "extra", "index", "matrix", "next", "text", "complex", "context"],
    "y": ["year", "your", "yield", "young", "system", "theory", "memory", "energy", "steady", "verify"],
    "z": ["zero", "zone", "zoom", "zeal", "zenith", "size", "prize", "organize", "realize", "analyze"],
    ";": ["ask;", "fall;", "first;", "next;", "clear;", "focus;", "note;", "ready;", "check;", "done;"],
    ",": ["one, two,", "fast, clear,", "calm, steady,", "first, second,", "plan, test,"],
    ".": ["stop.", "done.", "clear.", "exact.", "focus.", "ready.", "start.", "finish."],
}

HOME_ANCHOR_FOR_FINGER = {
    "L_PINKY": "a",
    "L_RING": "s",
    "L_MIDDLE": "d",
    "L_INDEX": "f",
    "THUMB": " ",
    "R_INDEX": "j",
    "R_MIDDLE": "k",
    "R_RING": "l",
    "R_PINKY": ";"
}


def analyze_user_weaknesses(telemetry_list: list, language: str = "en"):
    fmap = get_finger_map_for_language(language)

    if not telemetry_list:
        return {
            "weak_keys": [],
            "slow_keys": [],
            "confusion_pairs": [],
            "finger_stats": {},
            "coach_summary": "Complete your first short lesson so Coach Kavi can map your finger reflexes and tailor custom practice lines!"
        }

    scored_keys = []
    confusion_pairs = []
    finger_agg = {}

    latencies = [t["avg_latency_ms"] for t in telemetry_list if t.get("total_attempts", 0) >= 3 and t.get("avg_latency_ms")]
    median_lat = sorted(latencies)[len(latencies) // 2] if latencies else 250.0

    for t in telemetry_list:
        k = t["expected_key"]
        if k == " ":
            continue
        hits = t.get("hits", 0)
        misses = t.get("misses", 0)
        total = hits + misses
        if total == 0:
            continue

        err_rate = (misses / total) * 100.0
        lat = t.get("avg_latency_ms") or 250.0
        lat_ratio = max(0.0, (lat - median_lat) / max(median_lat, 100.0))

        weakness_score = (err_rate * 2.2) + (min(misses, 30) * 1.8) + (lat_ratio * 15.0)

        finger = fmap.get(k, "R_INDEX")
        finger_label = FINGER_LABELS.get(finger, finger)

        if finger not in finger_agg:
            finger_agg[finger] = {
                "finger_code": finger,
                "finger_name": finger_label,
                "hits": 0,
                "misses": 0,
                "latencies": []
            }
        finger_agg[finger]["hits"] += hits
        finger_agg[finger]["misses"] += misses
        finger_agg[finger]["latencies"].append(lat)

        conf_map = t.get("confused_with") or {}
        top_confused_char = None
        top_confused_count = 0
        for typed_c, cnt in conf_map.items():
            if cnt > top_confused_count:
                top_confused_char = typed_c
                top_confused_count = cnt
            confusion_pairs.append({
                "expected": k,
                "typed": typed_c,
                "count": cnt,
                "finger": finger_label
            })

        scored_keys.append({
            "key": k,
            "hits": hits,
            "misses": misses,
            "total": total,
            "error_rate": round(err_rate, 1),
            "accuracy": round(100.0 - err_rate, 1),
            "avg_latency_ms": round(lat, 0),
            "weakness_score": round(weakness_score, 1),
            "finger_code": finger,
            "finger_name": finger_label,
            "top_confused_with": top_confused_char
        })

    scored_keys.sort(key=lambda x: x["weakness_score"], reverse=True)
    confusion_pairs.sort(key=lambda x: x["count"], reverse=True)

    weak_keys = [k for k in scored_keys if k["misses"] > 0 or k["error_rate"] > 4.0][:8]
    if not weak_keys:
        weak_keys = sorted(scored_keys, key=lambda x: x["avg_latency_ms"], reverse=True)[:5]

    slow_keys = sorted(scored_keys, key=lambda x: x["avg_latency_ms"], reverse=True)[:6]

    finger_stats = {}
    weakest_finger = None
    lowest_finger_acc = 101.0
    for f_code, fd in finger_agg.items():
        tot = fd["hits"] + fd["misses"]
        acc = round((fd["hits"] / tot) * 100.0, 1) if tot > 0 else 100.0
        avg_l = round(sum(fd["latencies"]) / len(fd["latencies"]), 0) if fd["latencies"] else 250
        finger_stats[f_code] = {
            "finger_code": f_code,
            "finger_name": fd["finger_name"],
            "hits": fd["hits"],
            "misses": fd["misses"],
            "accuracy": acc,
            "avg_latency_ms": avg_l
        }
        if tot >= 5 and acc < lowest_finger_acc:
            lowest_finger_acc = acc
            weakest_finger = fd["finger_name"]

    if weak_keys and weak_keys[0]["misses"] > 0:
        top_w = weak_keys[:3]
        keys_str = ", ".join([f"'{x['key']}' ({x['error_rate']}%)" for x in top_w])
        conf_note = ""
        if confusion_pairs:
            cp = confusion_pairs[0]
            conf_note = f" You occasionally press '{cp['typed']}' when aiming for '{cp['expected']}' ({cp['count']}x)."
        finger_note = f" Give extra attention to your {weakest_finger}." if weakest_finger else ""
        coach_summary = f"Coach Kavi spotted hesitation on {keys_str}.{conf_note}{finger_note} Click 'Train Weak Keys' to smooth them out!"
    else:
        coach_summary = "Wonderful rhythm! Your accuracy across practiced characters is super clean. Try a faster chapter or an Arcade Game!"

    return {
        "weak_keys": weak_keys,
        "all_scored_keys": scored_keys,
        "slow_keys": slow_keys,
        "confusion_pairs": confusion_pairs[:8],
        "finger_stats": finger_stats,
        "coach_summary": coach_summary
    }


def generate_remedial_drill(telemetry_list: list, custom_focus_keys: list = None, language: str = "en"):
    analysis = analyze_user_weaknesses(telemetry_list, language)
    weak_items = analysis["weak_keys"]
    fmap = get_finger_map_for_language(language)

    if custom_focus_keys:
        target_keys = [k.strip() for k in custom_focus_keys if k.strip()][:5]
    elif weak_items:
        target_keys = [w["key"] for w in weak_items[:4]]
    elif language in INDIAN_LANGUAGE_PACKS:
        km = INDIAN_LANGUAGE_PACKS[language]["keymap"]
        target_keys = [km["KeyK"]["main"], km["KeyJ"]["main"], km["KeyE"]["main"], km["KeyF"]["main"]]
    else:
        target_keys = ["f", "j", "d", "k", "e", "i"]

    conf_lookup = {}
    for w in weak_items:
        if w.get("top_confused_with") and w["top_confused_with"] != " ":
            conf_lookup[w["key"]] = w["top_confused_with"]

    drill_segments = []

    if language in INDIAN_LANGUAGE_PACKS:
        pack = INDIAN_LANGUAGE_PACKS[language]
        km = pack["keymap"]
        anchor_r = km["KeyK"]["main"]
        for k in target_keys:
            drill_segments.append(f"{k}{anchor_r} {anchor_r}{k} {k}{k}")
            c = conf_lookup.get(k)
            if c and c != k:
                drill_segments.append(f"{k}{c} {c}{k}")
        vocab = pack["vocab"]
        all_native_words = vocab["home_words"] + vocab["top_words"] + vocab["bottom_words"] + vocab["conjunct_words"]
        matching_words = [w for w in all_native_words if any(tk in w for tk in target_keys)]
        if not matching_words:
            matching_words = all_native_words[:10]
        full_text = " ".join(drill_segments) + " " + " ".join(matching_words[:12])
    else:
        for k in target_keys:
            finger = fmap.get(k, "L_INDEX")
            anchor = HOME_ANCHOR_FOR_FINGER.get(finger, "f")
            if anchor == k:
                drill_segments.append(f"{k}{k} {k}{k}{k}")
            else:
                drill_segments.append(f"{anchor}{k}{anchor} {k}{anchor}{k}")
            c = conf_lookup.get(k)
            if c and c != k:
                drill_segments.append(f"{k}{c} {c}{k} {k}{k}{c}")

        word_pool = []
        for k in target_keys:
            words = WORD_BANK_BY_CHAR.get(k.lower(), [])
            if words:
                word_pool.extend(words[:5])
        if not word_pool:
            word_pool = ["focus", "steady", "rhythm", "practice", "accuracy", "control", "smooth", "precise"]
        selected_words = [word_pool[(i * 3) % len(word_pool)] for i in range(min(16, len(word_pool)))]
        full_text = " ".join(drill_segments) + " " + " ".join(selected_words) + "."

    keys_display = ", ".join(target_keys)
    return {
        "id": f"remedial_{language}",
        "title": f"Personal Coach Workout: [{keys_display}]",
        "type": "remedial",
        "new_keys": target_keys,
        "target_wpm": 18,
        "min_accuracy": 90,
        "tip": f"Custom workout crafted from your recent keystrokes to build effortless confidence on: {keys_display}",
        "text": full_text.strip(),
        "focus_keys": target_keys,
        "analysis": analysis
    }
