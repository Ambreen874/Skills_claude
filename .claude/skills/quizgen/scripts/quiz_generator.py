#!/usr/bin/env python3
"""
Quiz Generator - Generates MCQs from educational text
"""

import re
import random

class QuizGenerator:
    def __init__(self):
        # Common keywords that often indicate important concepts
        self.key_indicators = [
            r'\bis\s+defined\s+as\b',
            r'\brefers\s+to\b',
            r'\bcharacterized\s+by\b',
            r'\bconsists\s+of\b',
            r'\bincludes\b',
            r'\bhas\b',
            r'\bcontains\b',
            r'\bprocess\s+by\s+which\b',
            r'\bthe\s+purpose\s+of\b',
            r'\bused\s+to\b',
            r'\bknown\s+for\b',
            r'\boccurs\s+when\b',
            r'\bresults\s+in\b',
            r'\bcauses\b',
            r'\bleads\s+to\b'
        ]

    def identify_key_concepts(self, text):
        """Identify key concepts from the text"""
        concepts = []

        # Look for sentences with key indicators
        sentences = re.split(r'[.!?]+', text)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 5:  # Skip very short fragments
                continue

            # Add the sentence as a potential concept
            concepts.append(sentence)

        return concepts

    def generate_mcq(self, concept, all_concepts):
        """Generate a single MCQ from a concept"""
        # This is a simplified version - a real implementation would be more sophisticated
        # For now, we'll just create a placeholder question based on the concept

        # Extract potential question elements from the concept
        words = concept.split()

        # Create a question based on the concept
        question = self.create_question_from_concept(concept, words)

        # Generate correct answer (it's part of the concept)
        correct_answer = self.extract_correct_answer(concept, words)

        # Generate 3 incorrect answers (distractors) from other concepts
        distractors = self.generate_distractors(concept, all_concepts, 3)

        # Combine correct answer with distractors
        all_options = [correct_answer] + distractors
        random.shuffle(all_options)

        return {
            'question': question,
            'options': all_options,
            'correct_answer': correct_answer
        }

    def create_question_from_concept(self, concept, words):
        """Create a question from the concept"""
        # This is a simplified implementation
        # In a real implementation, this would use NLP to identify question patterns
        if 'is' in words and 'a' in words:
            # Likely a definition - create a "what is X" question
            for i, word in enumerate(words):
                if word.lower() == 'is' and i > 0:
                    subject = words[i-1]
                    return f"{subject} is a type of:"

        # Default fallback
        return f"What does this statement describe: {concept.strip()[:50]}..."

    def extract_correct_answer(self, concept, words):
        """Extract the correct answer from the concept"""
        # Simplified implementation
        return concept.strip()

    def generate_distractors(self, main_concept, all_concepts, count):
        """Generate incorrect but plausible answers"""
        distractors = []

        for concept in all_concepts:
            if concept != main_concept and len(distractors) < count:
                # Add the concept as a distractor if it's different
                distractors.append(concept.strip())

        # If we don't have enough distractors, pad with generic options
        while len(distractors) < count:
            distractors.append("Other concept")

        return distractors[:count]

    def generate_quiz(self, text, num_questions=None):
        """Generate a complete quiz from the text"""
        concepts = self.identify_key_concepts(text)

        if not concepts:
            return "No concepts found in the provided text."

        # If no number specified, generate as many as possible
        if num_questions is None:
            num_questions = len(concepts)
        else:
            num_questions = min(num_questions, len(concepts))

        quiz = []
        for i in range(num_questions):
            if i < len(concepts):
                mcq = self.generate_mcq(concepts[i], concepts)
                quiz.append({
                    'number': i + 1,
                    'question': mcq['question'],
                    'options': mcq['options'],
                    'correct_answer': mcq['correct_answer']
                })

        return quiz

def format_quiz(quiz):
    """Format the quiz in the required output format"""
    result = []
    for item in quiz:
        result.append(f"{item['number']}. {item['question']}")
        for i, option in enumerate(item['options'], ord('a')):
            marker = " ✅" if option == item['correct_answer'] else ""
            result.append(f"   {chr(i)}) {option}{marker}")
        result.append("")  # Empty line after each question

    return "\n".join(result).strip()

def main():
    generator = QuizGenerator()

    import sys
    if len(sys.argv) > 1:
        # If input is provided as command line argument
        input_text = ' '.join(sys.argv[1:])
    else:
        # Read from stdin
        input_text = sys.stdin.read().strip()

    # Check if user specified number of questions
    num_questions = None
    # This is a simplified implementation - in a real version you'd parse for question count

    quiz = generator.generate_quiz(input_text, num_questions)
    formatted_quiz = format_quiz(quiz)
    print(formatted_quiz)

if __name__ == "__main__":
    main()