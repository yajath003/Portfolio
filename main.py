from application import create_app
from self.models import Projects, Certifications, Skills, Work, Resume, Education
app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
