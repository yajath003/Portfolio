from application import db
from sqlalchemy import LargeBinary
from datetime import date

class Projects(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    project_name = db.Column(db.String(80), nullable=False, unique=True)
    project_description = db.Column(db.String(900), nullable=False)
    live_link = db.Column(db.String(500))
    git_link = db.Column(db.String(500), nullable=False)
    image = db.Column(db.LargeBinary)


class Certifications(db.Model):
    __tablename__ = 'certifications'
    certification_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    certification_name = db.Column(db.String(80), nullable=False, unique=True)
    certification_description = db.Column(db.String(900), nullable=False)
    drive_link = db.Column(db.String(500))
    certificate = db.Column(db.LargeBinary)


class Skills(db.Model):
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    skill_name = db.Column(db.String(80), nullable=False, unique=True)
    skill_type = db.Column(db.String(900), nullable=False)
    logo = db.Column(db.LargeBinary)


class Work(db.Model):
    __tablename__ = 'work'
    work_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    work_name = db.Column(db.String(80), nullable=False, unique=True)
    work_description = db.Column(db.String(900), nullable=False, unique=True)
    work_type = db.Column(db.String(900), nullable=False)
    certificate = db.Column(db.LargeBinary)
    drive_link = db.Column(db.String(500))


class Resume(db.Model):
    __tablename__ = 'resume'
    resume_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    resume_file = db.Column(db.LargeBinary)


class Education(db.Model):
    __tablename__ = 'education'
    education_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    education_name = db.Column(db.String(500), nullable=False, unique=True)
    start_date = db.Column(db.DATE, nullable=False)
    end_date = db.Column(db.Date)
    description = db.Column(db.String(500), unique=True)
    logo = db.Column(db.LargeBinary)
