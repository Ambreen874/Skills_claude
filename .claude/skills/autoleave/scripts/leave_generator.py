#!/usr/bin/env python3
"""
AutoLeave - Automatic Leave Application Generator
"""

import re

class LeaveApplicationGenerator:
    def __init__(self):
        self.leave_types = {
            'medical': ['sick', 'illness', 'doctor', 'medical', 'health', 'fever', 'cold', 'surgery', 'treatment',
                       'appointment', 'therapy', 'hospital', 'clinic', 'examination', 'consultation', 'minor surgery'],
            'personal': ['family', 'emergency', 'personal', 'urgent', 'matter', 'private', 'home', 'relative',
                        'parent', 'child', 'spouse', 'wedding', 'event', 'ceremony'],
            'vacation': ['vacation', 'holiday', 'break', 'travel', 'trip', 'rest', 'relaxation', 'annual leave',
                        'time off', 'getaway', 'leisure', 'recreation'],
            'bereavement': ['death', 'funeral', 'mourning', 'loss', 'passed away', 'grief', 'deceased',
                           'condolences', 'memorial', 'burial'],
            'maternity': ['baby', 'child', 'birth', 'delivery', 'newborn', 'expecting', 'pregnant',
                         'childcare', 'parental', 'adoption'],
            'training': ['training', 'workshop', 'seminar', 'conference', 'certification', 'course',
                        'professional development', 'skill', 'education', 'learning']
        }

    def identify_leave_type(self, reason):
        """Identify the type of leave based on the reason"""
        reason_lower = reason.lower()

        for leave_type, keywords in self.leave_types.items():
            for keyword in keywords:
                if keyword in reason_lower:
                    return leave_type

        # Default to personal if no specific type is identified
        return 'personal'

    def generate_subject_line(self, leave_type):
        """Generate an appropriate subject line based on leave type"""
        subjects = {
            'medical': 'Leave Application - Medical Appointment',
            'personal': 'Personal Leave Request',
            'vacation': 'Annual Leave Request',
            'bereavement': 'Bereavement Leave Request',
            'maternity': 'Maternity/Paternity Leave Request',
            'training': 'Training Leave Request'
        }

        return subjects.get(leave_type, 'Leave Application Request')

    def generate_template(self, org_name, reason, days, leave_type):
        """Generate the leave application based on the identified type"""
        subject = self.generate_subject_line(leave_type)

        # Get the appropriate template based on leave type
        templates = {
            'medical': self._medical_template,
            'personal': self._personal_template,
            'vacation': self._vacation_template,
            'bereavement': self._bereavement_template,
            'maternity': self._maternity_template,
            'training': self._training_template
        }

        template_func = templates.get(leave_type, self._personal_template)
        return template_func(org_name, reason, days, subject)

    def _medical_template(self, org_name, reason, days, subject):
        """Generate medical leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I am writing to formally request a leave of absence for medical reasons. I need to attend to a scheduled medical appointment/procedure that requires {days} day(s) off from [DATE] to [DATE].

Accordingly, I am requesting {days} days of medical leave from {org_name}. I will ensure that all urgent matters are addressed before my leave begins, and I will coordinate with my colleagues to manage any immediate responsibilities.

Thank you for your consideration.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def _personal_template(self, org_name, reason, days, subject):
        """Generate personal leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I would like to formally request a leave of absence due to urgent personal matters that require my immediate attention. I need to be away from [DATE] to [DATE] for {days} day(s).

Therefore, I am applying for {days} days of personal leave from {org_name}. I will complete all pending tasks before my departure and ensure a smooth transition of responsibilities to my colleagues.

I appreciate your understanding.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def _vacation_template(self, org_name, reason, days, subject):
        """Generate vacation leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I am writing to formally request my annual leave/vacation time. I would like to take {days} day(s) off from [DATE] to [DATE] for rest and relaxation.

Accordingly, I am requesting {days} days of vacation leave from {org_name}. I have planned my schedule to ensure that all projects are up to date and that my duties are covered during my absence. I will be available via email for any urgent matters if necessary.

Your approval would be greatly appreciated.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def _bereavement_template(self, org_name, reason, days, subject):
        """Generate bereavement leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I am writing to inform you of a family bereavement and to request compassionate leave. Due to a family loss, I need to take {days} day(s) off from [DATE] to [DATE] to attend to arrangements and be with my family during this difficult time.

Therefore, I am applying for {days} days of bereavement leave from {org_name}. I will return to my duties as soon as possible and will coordinate with my team to address any urgent matters upon my return.

Thank you for your understanding and support during this time.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def _maternity_template(self, org_name, reason, days, subject):
        """Generate maternity/paternity leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I am writing to formally request maternity/paternity leave. I anticipate needing {days} day(s) off starting from [DATE] for [actual duration when confirmed].

Accordingly, I am requesting {days} days of parental leave from {org_name}. I am working with my supervisor to ensure a smooth transition of my responsibilities and will provide updated information regarding my return date as soon as possible.

Thank you for your consideration and support.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def _training_template(self, org_name, reason, days, subject):
        """Generate training/professional development leave application"""
        return f"""To: {org_name} Administration
Subject: {subject}

Dear Sir/Madam,

I would like to apply for leave to attend professional development activities, which will enhance my professional skills and benefit my role at {org_name}. I need to be absent for {days} day(s) from [DATE] to [DATE].

Accordingly, I am requesting {days} days of training leave. The knowledge gained from this opportunity will contribute to my performance and the organization's objectives. I will coordinate with my team to minimize any disruption during my absence.

I appreciate your support for my professional development.

Sincerely,
[Your Name]
[Your Position/Department]
[Contact Information]"""

    def generate_application(self, org_name, reason, days):
        """Main method to generate the complete leave application"""
        leave_type = self.identify_leave_type(reason)
        return self.generate_template(org_name, reason, days, leave_type)

def main():
    generator = LeaveApplicationGenerator()

    import sys
    if len(sys.argv) >= 4:
        # If input is provided as command line arguments
        org_name = sys.argv[1]
        reason = sys.argv[2]
        try:
            days = int(sys.argv[3])
        except ValueError:
            days = 1  # default to 1 day if invalid number provided
    else:
        # Print usage if insufficient arguments
        print("Usage: python leave_generator.py <organization_name> <reason_for_leave> <number_of_days>")
        print("Example: python leave_generator.py 'ABC Company' 'Need to visit doctor for checkup' 3")
        sys.exit(1)

    application = generator.generate_application(org_name, reason, days)
    print(application)

if __name__ == "__main__":
    main()