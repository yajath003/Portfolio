from flask import Blueprint, render_template, redirect, session, request, url_for, flash, send_file, current_app
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
import base64
from io import BytesIO
import os


from self.models import Projects, Certifications, Work, Skills, Resume, Education
from application import db

self_app = Blueprint('self_app', __name__)


@self_app.route('/', methods=['GET', 'POST'])
def index():
    resume = Resume.query.first()
    session['admin'] = False
    return render_template('index.html', resume_available=bool(resume))


@self_app.route('/projects', methods=['GET', 'POST'])
def projects():
    pros = Projects.query.all()
    images = []
    for project in pros:
        if project.image:
            img = base64.b64encode(project.image).decode('utf-8')
            images.append(img)
    session['admin'] = False
    return render_template('projects.html', projects=pros, images=images, zip=zip)


@self_app.route('/skills', methods=['GET', 'POST'])
def skills():
    skills = Skills.query.all()
    images = []
    for skill in skills:
        if skill.logo:
            img = base64.b64encode(skill.logo).decode('utf-8')
            images.append(img)
    session['admin'] = False
    return render_template('skills.html', skills=skills, images=images, zip=zip)


@self_app.route('/certification', methods=['GET', 'POST'])
def certification():
    certifications = Certifications.query.all()
    images = []
    for certification in certifications:
        if certification.certificate:
            img = base64.b64encode(certification.certificate).decode('utf-8')
            images.append(img)
    session['admin'] = False
    return render_template('certification.html', certifications=certifications, images=images, zip=zip)


@self_app.route('/work', methods=['GET', 'POST'])
def work():
    works = Work.query.all()
    images = []
    for work in works:
        if work.certificate:
            img = base64.b64encode(work.certificate).decode('utf-8')
            images.append(img)
    session['admin'] = False
    return render_template('work.html', works=works, images=images, zip=zip)


@self_app.route('/projects_upload', methods=['POST', 'GET'])
def projects_upload():
    if session['admin']:
        if request.method == 'POST':
            project_name = request.form.get('project_name')
            project_description = request.form.get('description')
            render_link = request.form.get('render_link')
            github_link = request.form.get('github_link')
            image = None
            project_image = request.files.get('project_image')
            if project_image and project_image.filename != '':
                image = project_image.read()
                project_image.seek(0)
            project = Projects(
                project_name=project_name,
                project_description=project_description,
                live_link=render_link,
                git_link=github_link,
                image=image
            )
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('self_app.creator'))
        return render_template('projects_upload.html')


@self_app.route('/creator')
def creator():
    if session['admin']:
        return render_template('creator.html')


@self_app.route('/certification_upload', methods=['POST', 'GET'])
def certification_upload():
    if session['admin']:
        if request.method == 'POST':
            certification_name = request.form.get('cert_name')
            certification_description = request.form.get('description')
            drive_link = request.form.get('cert_url')
            image = None
            certificate_file = request.files.get('certificate_file')
            if certificate_file and certificate_file.filename != '':
                image = certificate_file.read()
                certificate_file.seek(0)
            certificate = Certifications(
                certification_name=certification_name,
                certification_description=certification_description,
                drive_link=drive_link,
                certificate=image
            )
            db.session.add(certificate)
            db.session.commit()
            return redirect(url_for('self_app.creator'))
        return render_template('certification_upload.html')


@self_app.route('/skill_upload', methods=['POST', 'GET'])
def skill_upload():
    if session['admin']:
        if request.method == 'POST':
            skill_name = request.form.get('skill_name')
            skill_type = request.form.get('skill_type')
            image = None
            skill_image = request.files.get('skill_image')
            if skill_image and skill_image.filename != '':
                image = skill_image.read()
                skill_image.seek(0)
            skill = Skills(
                skill_name=skill_name,
                skill_type=skill_type,
                logo=image
            )
            db.session.add(skill)
            db.session.commit()
            return redirect(url_for('self_app.creator'))
        return render_template('skill_upload.html')


@self_app.route('/work_upload', methods=['POST', 'GET'])
def work_upload():
    if session['admin']:
        if request.method == 'POST':
            work_name = request.form.get('work_name')
            work_description = request.form.get('description')
            work_type = request.form.get('work_type')
            image = None
            certificate = request.files.get('certificate')
            if certificate and certificate.filename != '':
                image = certificate.read()
                certificate.seek(0)
            drive_link = request.form.get('drive_link')
            job = Work(
                work_name=work_name,
                work_description=work_description,
                work_type=work_type,
                certificate=image,
                drive_link=drive_link
            )
            db.session.add(job)
            db.session.commit()
            return redirect(url_for('self_app.creator'))
        return render_template('work_upload.html')


@self_app.route('/education_upload', methods=['POST', 'GET'])
def education_upload():
    if session['admin']:
        return render_template('education_upload.html')


@self_app.route('/resume_upload', methods=['POST', 'GET'])
def resume_upload():
    if session['admin']:
        if request.method == 'POST':
            image = None
            resume_file = request.files.get('resume_file')
            if resume_file and resume_file.filename != '':
                image = resume_file.read()
                resume_file.seek(0)
            Resume.query.delete()
            db.session.commit()
            res = Resume(
                resume_file=image
            )
            db.session.add(res)
            db.session.commit()
            return redirect(url_for('self_app.creator'))
        return render_template('resume_upload.html')


@self_app.route('/creator_login', methods=['POST', 'GET'])
def creator_login():
    if request.method == 'POST':
        pwd = request.form.get('access_key')
        hashed_pwd = current_app.config['CREATOR_HASHED_PASSWORD']
        if check_password_hash(hashed_pwd, pwd):
            session['admin'] = True
            return redirect(url_for('self_app.creator'))
    return render_template('creator_login.html')


@self_app.route('/download_resume')
def download_resume():
    resume = Resume.query.first()
    if resume and resume.resume_file:
        return send_file(
            BytesIO(resume.resume_file),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='Yajath_Kandregula_Resume.pdf'
        )
    return "Resume not available", 404


if __name__ == '__main__':
    app.run(debug=True)
