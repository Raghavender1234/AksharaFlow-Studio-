# 🏪 Microsoft Store Partner Center Submission Guide for AksharaFlow Studio

This guide contains every exact field, switch, logo, and copy-paste description you need to publish **AksharaFlow Studio** (`AksharaFlow_Studio.exe`) on the **Microsoft Store**.

---

## Step 1: Reserve Your App Name in Partner Center
1. Open [Microsoft Partner Center — Apps and Games](https://partner.microsoft.com/en-us/dashboard/apps-and-games/overview).
2. Click **"+ New product"** $\rightarrow$ Select **"EXE or MSI"** (Win32 Desktop App).
3. Enter the App Name:
   - **`AksharaFlow Studio`** *(or `AksharaFlow - 14 Script Typing Tutor`)*
4. Click **Reserve product name**.

---

## Step 2: Packages (Win32 `.exe` Configuration)
When you upload `AksharaFlow_Studio.exe` to your **GitHub Release (`v1.0.0`)**, copy the direct HTTPS download link to `AksharaFlow_Studio.exe` (e.g., `https://github.com/<your-username>/AksharaFlow-Studio/releases/download/v1.0.0/AksharaFlow_Studio.exe`).

In Partner Center $\rightarrow$ **Packages**:
- **Package URL (HTTPS):** Paste your GitHub Release direct download URL for `AksharaFlow_Studio.exe`
- **Architecture:** `x64`
- **Installer parameters (Silent Install Switch):**
  ```text
  /S
  ```
  *(Note: `AksharaFlow_Studio.exe` has built-in `/S` and `--install` silent installation support! When Microsoft Store runs `AksharaFlow_Studio.exe /S`, it silently installs into `%LOCALAPPDATA%\Programs\AksharaFlowStudio`, creates Start Menu & Desktop shortcuts, registers in Windows Add/Remove Programs, and returns exit code `0`.)*
- **Installer behavior:** `User` (Per-user installation — does not require UAC Administrator elevation!)
- **Return codes:**
  - `0` = `Success`

---

## Step 3: Properties & Age Rating
- **Category:** `Education`
- **Subcategory:** `Language` (or `Instructional tools`)
- **Price:** `Free` (100% Free Forever)
- **Age Rating:** `3+` / `Everyone` (No violence, no user-to-user chat, no personal data collection, 100% offline educational tool)
- **Privacy Policy Notes:**
  > AksharaFlow Studio operates 100% offline on the user's local device. It does not collect, transmit, or share any personal data, telemetry, or analytics over the internet. All learner typing progress is stored locally in `%LOCALAPPDATA%\AksharaFlowStudio`.

---

## Step 4: Store Listing (Copy & Paste Ready)

### Short Description
> Master touch-typing in English (QWERTY) and 13 Indian Languages (InScript)! Includes 237 step-by-step lessons, Coach Kavi's adaptive mistake clinic, dual-legend 3D keyboard & hand guides, and 3 smooth 60–144fps arcade typing games. 100% free & offline.

### Full Description
```text
AksharaFlow Studio ("Every Script. Every Finger. Free Forever.") is a complete, 100% free offline desktop touch-typing coach and arcade game studio for English (QWERTY) and 13 Indian Language Scripts (Official Government of India InScript Standard).

Whether you are a student, professional, government exam aspirant, or multilingual writer, AksharaFlow Studio takes you from basic Home Row anchor keys to numbers, punctuation marks, conjuncts (samyuktaksharas), and full paragraphs with calm precision and joyful feedback.

KEY FEATURES:
• Zero-Password Instant Resume: Simply enter your name, choose your language script, and resume from your exact lesson, WPM speed history, and weak-key profile.
• 14 Supported Language Scripts (237 Progressive Lessons):
  1. English (QWERTY Standard)
  2. Hindi (हिन्दी - Devanagari InScript)
  3. Marathi (मराठी - Devanagari InScript)
  4. Sanskrit (संस्कृतम् - Devanagari InScript)
  5. Bengali (বাংলা - Bengali InScript)
  6. Punjabi (ਪੰਜਾਬੀ - Gurmukhi InScript)
  7. Gujarati (ગુજરાતી - Gujarati InScript)
  8. Odia (ଓଡ଼ିଆ - Odia InScript)
  9. Tamil (தமிழ் - Tamil InScript)
  10. Telugu (తెలుగు - Telugu InScript)
  11. Kannada (ಕನ್ನಡ - Kannada InScript)
  12. Malayalam (മലയാളം - Malayalam InScript)
  13. Assamese (অসমীয়া - Assamese InScript)
  14. Urdu (اردو - InScript / Standard)

• Built-In Smart Auto-InScript Mapper + Native Setup Guides:
  Displays clear instructions in your chosen Indian language to turn on your Windows InScript keyboard (Win + Space) — AND includes an automatic software InScript mapper so you can type Indian scripts immediately even from a standard English keyboard setting!

• Coach Kavi's Adaptive Mistake Clinic:
  Analyzes every keystroke's error rate, reaction speed (ms), and key confusion pairs to generate personalized weak-key practice drills for your exact fingers.

• Dual-Legend 3D Walnut Keyboard & Ergonomic Hand Guides:
  Shows both the Indian InScript character, Shift character, and physical QWERTY key alongside left and right hand finger indicators.

• 3 Built-In Multi-Script Arcade Typing Games:
  - Bubble Pop Reflex: Pop rising meadow bubbles with Golden Boss Bubbles targeting your weakest keys.
  - Meteor Laser Defense: Lock plasma turrets onto falling words and numbers.
  - Nitro Type Sprint: Race your roadster against 3 WPM-calibrated pace cars on full punctuated sentences.
```

### Search Keywords (Max 7)
1. `typing tutor`
2. `touch typing`
3. `hindi typing inscript`
4. `indian language typing`
5. `typing games`
6. `learn typing`
7. `typing speed test`

---

## Step 5: Store Logos & Visual Assets
Your pre-sized PNG logos are ready in:
- `c:\Users\brred\Desktop\TypingMaster_Pro\assets\store_logos\StoreLogo_300x300.png`
- `c:\Users\brred\Desktop\TypingMaster_Pro\assets\store_logos\Square150x150Logo.png`
- `c:\Users\brred\Desktop\TypingMaster_Pro\assets\store_logos\Square310x310Logo.png`
