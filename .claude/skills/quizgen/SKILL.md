---
name: quizgen
description: Help students prepare for exams by converting study material into quiz questions. Use when you need to transform educational text into multiple-choice questions (MCQs) with correct answers and plausible distractors for exam preparation.
---

# QuizGen

## Purpose
Help students prepare for exams by converting study material into quiz questions.

## Repeatable Cognitive Task
- Identify key concepts from educational text
- Generate assessment questions

## Input
- Plain educational text (notes, lecture content, document text)
- Optional: number of questions (default = as many questions you can make)

## Output
- A quiz containing only Multiple Choice Questions (MCQs)
- Each MCQ must include:
  - One correct answer
  - Three plausible incorrect options
- Clearly mark the correct answer

## Rules
- Use only the provided text
- Do not add explanations
- Do not include external knowledge
- Keep questions exam-oriented
- One input produces one quiz

## Question Generation Guidelines
- Focus on key concepts, definitions, facts, and important details from the text
- Create questions that test comprehension, not just memorization
- Make incorrect options (distractors) plausible but clearly wrong
- Ensure the correct answer is unambiguously correct based on the provided text
- Use various question formats:
  - Definition questions: "X is defined as:"
  - Identification questions: "Which of the following is a characteristic of X?"
  - Relationship questions: "X is related to Y in which way?"
  - Application questions: "An example of X would be:"

## Distractor Quality Standards
- Distractors should be grammatically consistent with the correct answer
- Distractors should be similar in length to the correct answer
- Distractors should be plausible enough to challenge students who haven't studied
- Avoid obviously incorrect or humorous distractors

## Example
Input: "Artificial Intelligence is a branch of computer science that focuses on building intelligent systems."

Output:
1. Artificial Intelligence is a branch of:
   a) Biology
   b) Computer Science ✅
   c) Mathematics
   d) Physics

## Scope
- Keep implementation small and focused
- Generate high-quality questions that align with the provided content
- Maintain academic integrity by only using information from the source text