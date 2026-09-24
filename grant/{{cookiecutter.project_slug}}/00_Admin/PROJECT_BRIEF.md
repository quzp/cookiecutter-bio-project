# PROJECT BRIEF

Project ID: {{ cookiecutter.project_id }}
Project title: {{ cookiecutter.project_name }}
Short title:

PI: {{ cookiecutter.pi_name }}
Institution: {{ cookiecutter.institution }}
Collaborators / MPIs:

Sponsor: {{ cookiecutter.sponsor }}
Mechanism: {{ cookiecutter.mechanism }}
NOFO/RFA number: {{ cookiecutter.nofo_number }}
NOFO/RFA URL: {{ cookiecutter.nofo_url }}
Application type (new / resubmission / renewal / revision): {% if cookiecutter.is_resubmission == 'yes' %}resubmission{% else %}new{% endif %}
Deadline: {{ cookiecutter.deadline }}
OSP internal deadline: {{ cookiecutter.internal_deadline }}

Target IC / program: {{ cookiecutter.target_program }}
Program officer: {{ cookiecutter.program_officer }}
Target study section / review panel: {{ cookiecutter.study_section }}

Project period: {{ cookiecutter.project_period }}
Budget ceiling: {{ cookiecutter.budget_ceiling }}
Requested direct costs:

Clinical trial:
Human subjects / IRB status:
Vertebrate animals:
Human iPSC / organoids (lines, authentication plan):
Genomic data (DMS / GDS):
Foreign component:

Sponsor AI-use policy (from P0):
Institutional AI certification required? (from OSP):

Scientific field: {{ cookiecutter.scientific_field }}
Disease / problem: {{ cookiecutter.disease_problem }}
Model system: {{ cookiecutter.model_system }}
Central biological question: {{ cookiecutter.central_biological_question }}

Coordinator assistant: {{ cookiecutter.coordinator_assistant }}
Analysis tool: {{ cookiecutter.analysis_tool }}
Analysis repository: {{ cookiecutter.analysis_repo }}
Reference library: {{ cookiecutter.reference_library }}

Key preliminary datasets:
1.
2.
3.
