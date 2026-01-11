---
name: autoleave
description: Generate a professional leave application draft that adapts its tone and wording based on the reason for leave. Use when you need to create a formal leave application with appropriate language based on the leave reason, number of days, and organization name.
---

# AutoLeave

## Purpose
Generate a professional leave application draft that adapts its tone and wording based on the reason for leave.

## Repeatable Cognitive Task
- Analyze the reason for leave
- Select appropriate formal language
- Generate a structured leave application draft

## Input
- Organization or Institution name
- Reason for leave (free text)
- Number of leave days

## Output
- A complete, editable leave application draft
- Tone and subject line adjusted according to the reason

## Rules
- Use formal and respectful language
- Automatically infer leave type (medical, personal, academic, etc.)
- Do NOT ask follow-up questions
- Do NOT add unnecessary personal details
- One input produces exactly one draft

## Draft Structure
- Address
- Subject (reason-aware)
- Salutation
- Body
- Closing with placeholders

## Leave Type Recognition
The skill identifies different types of leave from the reason text:

### Medical Leave
Keywords: sick, illness, doctor, medical, health, fever, cold, surgery, treatment, appointment
Tone: Respectful, apologetic, brief explanation

### Personal Leave
Keywords: family, emergency, personal, urgent, matter, private, home
Tone: Professional, concise, minimal detail

### Academic/Vacation Leave
Keywords: vacation, holiday, break, travel, trip, rest, relaxation
Tone: Formal, polite, appreciative

### Bereavement Leave
Keywords: death, funeral, mourning, loss, passed away, grief
Tone: Somber, respectful, brief

### Maternity/Paternity Leave
Keywords: baby, child, birth, delivery, newborn, expecting, pregnant
Tone: Professional, informative, timeline-focused

## Language Guidelines

### Formal Opening Phrases
- "I am writing to formally request..."
- "I would like to apply for..."
- "I respectfully request..."

### Professional Closing Phrases
- "Thank you for your consideration."
- "I appreciate your understanding."
- "Your approval would be greatly appreciated."

### Transition Phrases
- "Accordingly, I am requesting..."
- "Therefore, I would like to request..."
- "For this reason, I am applying for..."

## Example Input/Output
Input:
- Organization: ABC University
- Reason: Need to visit doctor for minor surgery
- Days: 3

Output:
Subject: Leave Application - Medical Appointment

Dear Sir/Madam,

I am writing to formally request a leave of absence from [DATE] to [DATE] due to a scheduled medical procedure. I need to visit my doctor for a minor surgical procedure that requires some recovery time.

Accordingly, I am requesting 3 days of medical leave from ABC University. I will ensure that all pending responsibilities are addressed before my leave begins, and I will catch up on any missed work upon my return.

Thank you for your consideration.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]