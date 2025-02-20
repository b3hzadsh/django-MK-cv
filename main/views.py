from django.shortcuts import render

app_name = "main"


# Create your views here.
def index(request):
    context = {
        "name": "Behzad Shabanifard",
        "bio": "Hello! I am Behzad Shabanifard. I work as mobile and back-end developer ",
        "social_links": [
            {
                "name": "Twitter",
                "url": "https://www.twitter.com/b3hzadsh/",
                "class": "fab fa-twitter",
            },
            {
                "name": "Github",
                "url": "https://www.github.com/b3hzadsh/",
                "class": "fab fa-github-alt",
            },
            {
                "name": "Instagram",
                "url": "https://www.instagram.com/b3hzadsh/",
                "class": "fab fa-instagram",
            },
        ],
        "courses": [
            {"title": "Maktabkhooneh: Django", "description": "Django course 1287"},
        ],
        "skills": {
            "good": ["Python", "Dart", "Flutter"],
            "basic": ["Django", "SQL", "FastAPI"],
        },
        "languages": [
            {"name": "Persian", "proficiency": "Native speaker"},
            {"name": "English", "proficiency": "Proficient C1/C2"},
        ],
        "education": [
            {
                "institution": "Semnan University",
                "degree": "Bachelor Degree of Computer Engineering",
                "start_year": 2016,
                "end_year": 2020,
            },
        ],
        "experience": [
            {
                "company": "Yar Company",
                "position": "Mobile developer Intern",
                "start_date": "03.2019",
                "end_date": "06.2023",
                "tech_stack": "Dart / Flutter / SQL ",
                "responsibilities": [
                    "Develop mobile application for Yar departments",
                    "Implement UI based on received graphic design and requirements",
                    "Co-operate with the back-end team",
                ],
            },
        ],
    }
    return render(request, "index.html", context=context)
