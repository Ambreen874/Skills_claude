---
name: roman-urdu-to-urdu-writer
description: Convert Roman Urdu text into correct, readable Urdu script. Use when you need to transform informal Roman Urdu (using Latin characters) into proper Urdu script with correct spelling, grammar, and flow while preserving original meaning and emotional tone.
---

# Roman Urdu to Urdu Writer

## Purpose
Convert Roman Urdu text into correct, readable Urdu script, maintaining the original meaning and emotional tone.

## Input
- A string of Roman Urdu text (informal, poetic, conversational)

## Output
- The same text written in proper Urdu script
- Correct spelling, grammar, and flow
- Preserved original meaning and emotional tone

## Rules
- Do NOT add new words or lines
- Do NOT explain the output
- Only return the converted Urdu text
- Handle common Roman abbreviations appropriately
- Avoid literal word-by-word transliteration
- Avoid English words unless unavoidable

## Common Roman Urdu Abbreviations to Convert
- TU → تو
- mjy → مجھے
- tujy → تجھے
- bht → بہت
- ha / hai → ہے
- hn → ہیں
- aur → اور
- kya → کیا
- koi → کوئی
- jo → جو
- ke → کے
- ko → کو
- se → سے
- par → پر
- per → پر
- hy / hai → ہے
- hain → ہیں
- tha → تھا
- thay → تھے
- thi → تھی
- na → نہ
- nahi → نہیں
- ab → اب
- kal → کل
- aaj → آج
- hum → ہم
- tum → تم
- tumhara → تمہارا
- tumhari → تمہاری
- mujhe → مجھے
- tujhe → تجھے
- uske → اس کے
- iske → اس کے
- uska → اس کا
-iska → اس کا

## Conversion Process
1. Analyze the Roman Urdu input for meaning preservation
2. Apply appropriate Urdu spelling and grammar
3. Ensure natural Urdu sentence flow
4. Convert abbreviations to proper Urdu equivalents
5. Return only the converted Urdu text

## Example
Input: "Haqiqat kahon TU tujy khwab lgta ha"
Output: "حقیقت کہوں تو تجھے خواب لگتا ہے"

## Priorities
1. Meaning preservation
2. Correct Urdu spelling
3. Natural Urdu sentence flow