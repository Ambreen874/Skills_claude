#!/usr/bin/env python3
"""
Roman Urdu to Urdu Converter
This script converts Roman Urdu text to proper Urdu script.
"""

import re

class RomanUrduToUrduConverter:
    def __init__(self):
        # Basic conversion dictionary
        self.conversions = {
            # Pronouns
            r'\btu\b': 'تو',
            r'\btum\b': 'تم',
            r'\baap\b': 'آپ',
            r'\bmujhe\b': 'مجھے',
            r'\btujhe\b': 'تجھے',
            r'\bmujhy\b': 'مجھے',
            r'\btujhy\b': 'تجھے',
            r'\buse\b': 'اسے',
            r'\bise\b': 'اسے',

            # Common words
            r'\baur\b': 'اور',
            r'\baur\b': 'اور',
            r'\blekin\b': 'لیکن',
            r'\bpar\b': 'پر',
            r'\bper\b': 'پر',
            r'\bse\b': 'سے',
            r'\bke\b': 'کے',
            r'\bka\b': 'کا',
            r'\bki\b': 'کی',
            r'\bko\b': 'کو',
            r'\bkya\b': 'کیا',
            r'\bkoi\b': 'کوئی',
            r'\bjo\b': 'جو',
            r'\bna\b': 'نہ',
            r'\bnh\b': 'نہیں',
            r'\bnahi\b': 'نہیں',
            r'\bkyu\b': 'کیوں',
            r'\bkahan\b': 'کہاں',
            r'\bkab\b': 'کب',
            r'\bkis\b': 'کس',

            # Common abbreviations
            r'\bbht\b': 'بہت',
            r'\bbhut\b': 'بہت',
            r'\bthoda\b': 'تھوڑا',
            r'\bsab\b': 'سب',
            r'\bkuch\b': 'کچھ',
            r'\bhar\b': 'ہر',
            r'\bkon\b': 'کون',
            r'\bkoncay\b': 'کون سے',
            r'\bkonse\b': 'کون سے',
            r'\bkonca\b': 'کون سا',
            r'\bkonci\b': 'کون سی',

            # Verbs
            r'\bhy\b': 'ہے',
            r'\bhay\b': 'ہے',
            r'\bhai\b': 'ہے',
            r'\bhain\b': 'ہیں',
            r'\bhn\b': 'ہیں',
            r'\btha\b': 'تھا',
            r'\bthi\b': 'تھی',
            r'\bthe\b': 'تھے',
            r'\bthay\b': 'تھے',
            r'\bkr\b': 'کر',
            r'\bkro\b': 'کرو',
            r'\bkarein\b': 'کریں',
            r'\bkarunga\b': 'کروں گا',
            r'\bkarogi\b': 'کرو گی',
            r'\bjaana\b': 'جانا',
            r'\bjana\b': 'جانا',
            r'\bjao\b': 'جاؤ',
            r'\baana\b': 'آنا',
            r'\bao\b': 'آؤ',
            r'\baaya\b': 'آیا',
            r'\baaye\b': 'آۓ',
            r'\braha\b': 'رہا',
            r'\brehna\b': 'رہنا',
            r'\brahay\b': 'رہے',
            r'\brehti\b': 'رہتی',
            r'\brehte\b': 'رہتے',

            # Time related
            r'\bab\b': 'اب',
            r'\bkal\b': 'کل',
            r'\baaj\b': 'آج',
            r'\baj\b': 'آج',
            r'\bsubah\b': 'صبح',
            r'\bsham\b': 'شام',
            r'\braat\b': 'رات',
            r'\bdin\b': 'دن',
            r'\broz\b': 'روز',
            r'\bhafta\b': 'ہفتہ',
            r'\bmahina\b': 'ماہ',
            r'\bsaal\b': 'سال',

            # Common phrases and expressions
            r'\bshukriya\b': 'شکریہ',
            r'\bmeherbani\b': 'مہربانی',
            r'\bthaek\b': 'ٹھیک',
            r'\bbilkul\b': 'بالکل',
            r'\bzaroor\b': 'ضرور',
            r'\bzaruri\b': 'ضروری',
            r'\bsahi\b': 'صحیح',
            r'\bgalt\b': 'غلط',
            r'\basal\b': 'اصل',
            r'\bjhoot\b': 'وٹ',
            r'\bsach\b': 'سچ',
            r'\bpyaar\b': 'پیار',
            r'\bdosti\b': 'دوستی',
            r'\bghar\b': 'گھر',
            r'\bbaahar\b': 'باہر',
            r'\bandar\b': 'اندر',
            r'\bupar\b': 'اوپر',
            r'\bneechay\b': 'نیچے',
            r'\bagey\b': 'آگے',
            r'\bpeechay\b': 'پیچھے',
        }

    def convert(self, text):
        """
        Convert Roman Urdu text to Urdu script
        """
        if not text:
            return ""

        result = text

        # Apply conversions in order
        for pattern, replacement in self.conversions.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

        # Handle some special cases for common phrases
        result = re.sub(r'\bhaqiqat kahon', 'حقیقت کہوں', result, flags=re.IGNORECASE)
        result = re.sub(r'\bkhwab', 'خواب', result, flags=re.IGNORECASE)
        result = re.sub(r'\blgta', 'لگتا', result, flags=re.IGNORECASE)

        return result

def main():
    converter = RomanUrduToUrduConverter()

    import sys
    if len(sys.argv) > 1:
        # If input is provided as command line argument
        input_text = ' '.join(sys.argv[1:])
    else:
        # Read from stdin
        input_text = sys.stdin.read().strip()

    output = converter.convert(input_text)
    print(output)

if __name__ == "__main__":
    main()