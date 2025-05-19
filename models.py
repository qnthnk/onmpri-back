from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    first_last_name = db.Column(db.String(80), unique=False, nullable=False)
    second_last_name = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(15), unique=False, nullable=False)
    birthdate = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    facebook = db.Column(db.String(80), unique=False, nullable=True)
    instagram = db.Column(db.String(80), unique=False, nullable=True)
    x = db.Column(db.String(80), unique=False, nullable=True)
    state = db.Column(db.String(80), unique=False, nullable=False)
    colonia_mex = db.Column(db.String(80), unique=False, nullable=False)
    house_number = db.Column(db.String(10), unique=False, nullable=False)
    street = db.Column(db.String(80), unique=False, nullable=False)
    zip_code = db.Column(db.String(80), unique=False, nullable=False)
    nombre_municipio = db.Column(db.String(80), unique=False, nullable=False)
    latitude = db.Column(db.String(80), nullable=True)
    longitude = db.Column(db.String(80), nullable=True)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'), nullable=True)
    reset_code = db.Column(db.String(4), nullable=True)
    marriage_status = db.Column(db.String(80), unique=False, nullable=True) #AGREGADO
    age = db.Column(db.String(80), unique=False, nullable=True) #AGREGADO
    ocuppation = db.Column(db.String(80), unique=False, nullable=True) #AGREGADO
    phone_number_home = db.Column(db.String(80), unique=False, nullable=False) #AGREGADO
    phone_number_work = db.Column(db.String(80), unique=False, nullable=False) #AGREGADO
    phone_number_mobile = db.Column(db.String(80), unique=False, nullable=False) #AGREGADO
    reffered_by = db.Column(db.String(80), unique=False, nullable=True) #AGREGADO
    # curp = db.Column(db.String(18), unique=False, nullable=False) COMENTADO
    # phone_number = db.Column(db.String(80), unique=False, nullable=False) COMENTADO
    # blood_type = db.Column(db.String(5), unique=False, nullable=True) COMENTADO
    # allergy = db.Column(db.String(80), unique=False, nullable=True) COMENTADO
    # disease = db.Column(db.String(80), unique=False, nullable=True) COMENTADO
    # seccion = db.Column(db.String(10), unique=False, nullable=False) COMENTADO
    # distrito_federal = db.Column(db.String(80), unique=False, nullable=False) COMENTADO
    # distrito_local = db.Column(db.String(80), unique=False, nullable=False) COMENTADO
    # tipo_seccion = db.Column(db.String(80), unique=False, nullable=False) COMENTADO
    

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "first_last_name": self.first_last_name,
            "second_last_name": self.second_last_name,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "email": self.email,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "x": self.x,
            "state": self.state,
            "colonia_mex": self.colonia_mex,
            "house_number": self.house_number,
            "street": self.street,
            "zip_code": self.zip_code,
            "nombre_municipio": self.nombre_municipio,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "age": self.age, #AGREGADO
            "marriage_status": self.marriage_status, #AGREGADO
            "ocuppation": self.ocuppation, #AGREGADO
            "phone_number_home": self.phone_number_home, #AGREGADO
            "phone_number_work": self.phone_number_work, #AGREGADO
            "phone_number_mobile": self.phone_number_mobile, #AGREGADO
            "reffered_by": self.reffered_by #AGREGADO
            # "curp": self.curp,
            # "phone_number": self.phone_number,
            # "blood_type": self.blood_type,
            # "allergy": self.allergy,
            # "disease": self.disease,
            # "seccion": self.seccion,
            # "distrito_federal": self.distrito_federal,
            # "distrito_local": self.distrito_local,
            # "tipo_seccion": self.tipo_seccion,
            
        }

class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    report_url = db.Column(db.String(255), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    size = db.Column(db.Float, nullable=False)
    elapsed_time = db.Column(db.String(50), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # revisar si .UTC va o si cambiamos a .utcnow

class TodosLosReportes(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    report_url = db.Column(db.String(255), unique=True, nullable=False)  # La URL del reporte
    title = db.Column(db.String(255), nullable=False)  # El título del reporte
    size_megabytes = db.Column(db.Float, nullable=True)  # El tamaño del reporte en megabytes, puede ser NULL si no está disponible
    created_at = db.Column(db.DateTime, nullable=True)  # La fecha de creación, puede ser NULL si no está disponible

class AllCommentsWithEvaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    archivo_binario = db.Column(db.LargeBinary)


class Administrator(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    user = db.relationship('User', backref='administrator', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "organization_name": self.organization_name,
            "email": self.email
        }

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=False, nullable=False)
    role = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role,
            "phone_number": self.phone_number,
            "user_id": self.user_id
        }
    
class Billing(db.Model): #AGREGADO informacion de facturacion
    __tablename__ = 'billing'
    id = db.Column(db.Integer, primary_key=True)
    billing_name = db.Column(db.String(150), unique=False, nullable=False)
    rfc = db.Column(db.String(150), unique=False, nullable=False)
    billing_state = db.Column(db.String(80), unique=False, nullable=False)
    billing_colonia_mex = db.Column(db.String(80), unique=False, nullable=False)
    billing_house_number = db.Column(db.String(10), unique=False, nullable=False)
    billing_street = db.Column(db.String(80), unique=False, nullable=False)
    billing_zip_code = db.Column(db.String(80), unique=False, nullable=False)
    billing_nombre_municipio = db.Column(db.String(80), unique=False, nullable=False)
    billing_email = db.Column(db.String(150), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "billing_name": self.billing_name,
            "rfc": self.rfc,
            "billing_state": self.billing_state,
            "billing_colonia_mex": self.billing_colonia_mex,
            "billing_house_number": self.billing_house_number,
            "billing_street": self.billing_street,
            "billing_zip_code": self.billing_zip_code,
            "billing_nombre_municipio": self.billing_nombre_municipio,
            "billing_email": self.billing_email,
            "user_id": self.user_id
        }
    
class ClinicalResumeArFemale(db.Model): #AGREGADO resumen clinico esposa
    __tablename__ = 'clinical_resume_ar_female'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(150), unique=False, nullable=False)
    female_first_name = db.Column(db.String(80), unique=False, nullable=False)
    female_first_last_name = db.Column(db.String(80), unique=False, nullable=False)
    female_second_last_name = db.Column(db.String(80), unique=False, nullable=False)
    female_birthday = db.Column(db.String(80), unique=False, nullable=False)
    female_age = db.Column(db.String(80), unique=False, nullable=False)
    female_allergies = db.Column(db.String(80), unique=False, nullable=False)
    female_diseases = db.Column(db.String(80), unique=False, nullable=False)
    female_blood_type = db.Column(db.String(80), unique=False, nullable=False)
    female_height = db.Column(db.String(80), unique=False, nullable=False)
    female_weight = db.Column(db.String(80), unique=False, nullable=False)
    female_imc = db.Column(db.String(80), unique=False, nullable=False)
    female_app = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_surgeries = db.Column(db.String(280), unique=False, nullable=False)
    female_menarca = db.Column(db.String(80), unique=False, nullable=False)
    female_rythm_1 = db.Column(db.String(80), unique=False, nullable=False)
    female_rythm_2 = db.Column(db.String(80), unique=False, nullable=False)
    female_fum = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_pregnancies = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_births = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_abortions = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_cesareans = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_ectopics = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_molars = db.Column(db.String(80), unique=False, nullable=False)
    female_prev_ar_treatment = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "female_first_name": self.female_first_name,
            "female_first_last_name": self.female_first_last_name,
            "female_second_last_name": self.female_second_last_name,
            "female_birthday": self.female_birthday,
            "female_age": self.female_age,
            "female_allergies": self.female_allergies,
            "female_diseases": self.female_diseases,
            "female_blood_type": self.female_blood_type,
            "female_height": self.female_height,
            "female_weight": self.female_weight,
            "female_imc": self.female_imc,
            "female_app": self.female_app,
            "female_prev_surgeries": self.female_prev_surgeries,
            "female_menarca": self.female_menarca,
            "female_rythm_1": self.female_rythm_1,
            "female_rythm_2": self.female_rythm_2,
            "female_fum": self.female_fum,
            "female_prev_pregnancies": self.female_prev_pregnancies,
            "female_prev_births": self.female_prev_births,
            "female_prev_abortions": self.female_prev_abortions,
            "female_prev_cesareans": self.female_prev_cesareans,
            "female_prev_ectopics": self.female_prev_ectopics,
            "female_prev_molars": self.female_prev_molars,
            "female_prev_ar_treatment": self.female_prev_ar_treatment,
            "user_id": self.user_id
        }
    
class ClinicalResumeArMale(db.Model): #AGREGADO resumen clinico esposo
    __tablename__ = 'clinical_resume_ar_male'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(150), unique=False, nullable=False)
    male_first_name = db.Column(db.String(80), unique=False, nullable=False)
    male_first_last_name = db.Column(db.String(80), unique=False, nullable=False)
    male_second_last_name = db.Column(db.String(80), unique=False, nullable=False)
    male_birthday = db.Column(db.String(80), unique=False, nullable=False)
    male_age = db.Column(db.String(80), unique=False, nullable=False)
    male_allergies = db.Column(db.String(80), unique=False, nullable=False)
    male_diseases = db.Column(db.String(80), unique=False, nullable=False)
    male_blood_type = db.Column(db.String(80), unique=False, nullable=False)
    male_height = db.Column(db.String(80), unique=False, nullable=False)
    male_weight = db.Column(db.String(80), unique=False, nullable=False)
    male_imc = db.Column(db.String(80), unique=False, nullable=False)
    male_prev_ar_treatment = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "male_first_name": self.male_first_name,
            "male_first_last_name": self.male_first_last_name,
            "male_second_last_name": self.male_second_last_name,
            "male_birthday": self.male_birthday,
            "male_age": self.male_age,
            "male_allergies": self.male_allergies,
            "male_diseases": self.male_diseases,
            "male_blood_type": self.male_blood_type,
            "male_height": self.male_height,
            "male_weight": self.male_weight,
            "male_imc": self.male_imc,
            "male_prev_ar_treatment": self.male_prev_ar_treatment,
            "user_id": self.user_id
        }
    
class ClinicalResumeArFemaleInitialLabs(db.Model): #AGREGADO labs iniciales esposa REVISAR
    __tablename__ = 'clinical_resume_ar_female_initial_labs'
    id = db.Column(db.Integer, primary_key=True)
    histerosg = db.Column(db.String(280), unique=False, nullable=False)
    date = db.Column(db.String(150), unique=False, nullable=False)
    hormone_fsh = db.Column(db.String(80), unique=False, nullable=False)
    hormone_lh = db.Column(db.String(80), unique=False, nullable=False)
    hormone_e2 = db.Column(db.String(80), unique=False, nullable=False)
    hormone_prl = db.Column(db.String(80), unique=False, nullable=False)
    hormone_tsh = db.Column(db.String(80), unique=False, nullable=False)
    hormone_ham = db.Column(db.String(80), unique=False, nullable=False)
    laparo_histeroscopy = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "histerosg": self.histerosg,
            "date": self.date,
            "hormone_fsh": self.hormone_fsh,
            "hormone_lh": self.hormone_lh,
            "hormone_e2": self.hormone_e2,
            "hormone_prl": self.hormone_prl,
            "hormone_tsh": self.hormone_tsh,
            "hormone_ham": self.hormone_ham,
            "laparo_histeroscopy": self.laparo_histeroscopy,
            "user_id": self.user_id
        }
    
class FemaleDiagnosis(db.Model): #AGREGADO 
    __tablename__ = 'female_diagnosis'
    id = db.Column(db.Integer, primary_key=True)
    female_sterility = db.Column(db.String(80), unique=False, nullable=False)
    female_duration = db.Column(db.String(80), unique=False, nullable=False)
    female_etiology = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "female_sterility": self.female_sterility,
            "female_duration": self.female_duration,
            "female_etiology": self.female_etiology,
            "user_id": self.user_id
        }
    
class MaleDiagnosis(db.Model): #AGREGADO 
    __tablename__ = 'male_diagnosis'
    id = db.Column(db.Integer, primary_key=True)
    male_sterility = db.Column(db.String(80), unique=False, nullable=False)
    male_duration = db.Column(db.String(80), unique=False, nullable=False)
    male_etiology = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "male_sterility": self.male_sterility,
            "male_duration": self.male_duration,
            "male_etiology": self.male_etiology,
            "user_id": self.user_id
        }

class MaleEspermogram(db.Model): #AGREGADO labs iniciales esposa
    __tablename__ = 'male_espermogram'
    id = db.Column(db.Integer, primary_key=True)
    lab_name = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.String(150), unique=False, nullable=False)
    pickup_time = db.Column(db.String(80), unique=False, nullable=False)
    delivery_time = db.Column(db.String(80), unique=False, nullable=False)
    abstinence_time = db.Column(db.String(80), unique=False, nullable=False)
    total_volume = db.Column(db.String(80), unique=False, nullable=False)
    appearance = db.Column(db.String(80), unique=False, nullable=False)
    viscosity = db.Column(db.String(80), unique=False, nullable=False)
    gel_fragmentation = db.Column(db.String(80), unique=False, nullable=False)
    precap_volume = db.Column(db.String(80), unique=False, nullable=False)
    precap_counting = db.Column(db.String(80), unique=False, nullable=False)
    precap_counting_total = db.Column(db.String(80), unique=False, nullable=False)
    precap_counting_motility = db.Column(db.String(80), unique=False, nullable=False)
    precap_vitality = db.Column(db.String(80), unique=False, nullable=False)
    precap_leukocytes = db.Column(db.String(80), unique=False, nullable=False)
    precap_progressive_motility = db.Column(db.String(80), unique=False, nullable=False)
    precap_non_progressive_motility = db.Column(db.String(80), unique=False, nullable=False)
    precap_immotile = db.Column(db.String(80), unique=False, nullable=False)
    precap_total_motility = db.Column(db.String(80), unique=False, nullable=False)
    precap_normal_morphology = db.Column(db.String(80), unique=False, nullable=False)
    precap_abnormal_morphology = db.Column(db.String(80), unique=False, nullable=False)
    precap_erythrocytes = db.Column(db.String(80), unique=False, nullable=False)
    precap_bacteria = db.Column(db.String(80), unique=False, nullable=False)
    postcap_volume = db.Column(db.String(80), unique=False, nullable=False)
    postcap_counting = db.Column(db.String(80), unique=False, nullable=False)
    postcap_counting_total = db.Column(db.String(80), unique=False, nullable=False)
    postcap_counting_motility = db.Column(db.String(80), unique=False, nullable=False)
    postcap_vitality = db.Column(db.String(80), unique=False, nullable=False)
    postcap_leukocytes = db.Column(db.String(80), unique=False, nullable=False)
    postcap_progressive_motility = db.Column(db.String(80), unique=False, nullable=False)
    postcap_non_progressive_motility = db.Column(db.String(80), unique=False, nullable=False)
    postcap_immotile = db.Column(db.String(80), unique=False, nullable=False)
    postcap_total_motility = db.Column(db.String(80), unique=False, nullable=False)
    postcap_normal_morphology = db.Column(db.String(80), unique=False, nullable=False)
    postcap_abnormal_morphology = db.Column(db.String(80), unique=False, nullable=False)
    postcap_erythrocytes = db.Column(db.String(80), unique=False, nullable=False)
    postcap_bacteria = db.Column(db.String(80), unique=False, nullable=False)
    ph = db.Column(db.String(80), unique=False, nullable=False)
    dna_fragmentation = db.Column(db.String(80), unique=False, nullable=False)
    lab_comment = db.Column(db.String(80), unique=False, nullable=False)
   
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "lab_name": self.lab_name,
            "date": self.date,
            "pickup_time": self.pickup_time,
            "delivery_time": self.delivery_time,
            "abstinence_time": self.abstinence_time,
            "total_volume": self.total_volume,
            "appearance": self.appearance,
            "viscosity": self.viscosity,
            "gel_fragmentation": self.gel_fragmentation,
            "precap_volume": self.precap_volume,
            "precap_counting": self.precap_counting,
            "precap_counting_total": self.precap_counting_total,
            "precap_counting_motility": self.precap_counting_motility,
            "precap_vitality": self.precap_vitality,
            "precap_leukocytes": self.precap_leukocytes,
            "precap_progressive_motility": self.precap_progressive_motility,
            "precap_non_progressive_motility": self.precap_non_progressive_motility,
            "precap_immotile": self.precap_immotile,
            "precap_total_motility": self.precap_total_motility,
            "precap_normal_morphology": self.precap_normal_morphology,
            "precap_abnormal_morphology": self.precap_abnormal_morphology,
            "precap_erythrocytes": self.precap_erythrocytes,
            "precap_bacteria": self.precap_bacteria,
            "postcap_volume": self.postcap_volume,
            "postcap_counting": self.postcap_counting,
            "postcap_counting_total": self.postcap_counting_total,
            "postcap_counting_motility": self.postcap_counting_motility,
            "postcap_vitality": self.postcap_vitality,
            "postcap_leukocytes": self.postcap_leukocytes,
            "postcap_progressive_motility": self.postcap_progressive_motility,
            "postcap_non_progressive_motility": self.postcap_non_progressive_motility,
            "postcap_immotile": self.postcap_immotile,
            "postcap_total_motility": self.postcap_total_motility,
            "postcap_normal_morphology": self.postcap_normal_morphology,
            "postcap_abnormal_morphology": self.postcap_abnormal_morphology,
            "postcap_erythrocytes": self.postcap_erythrocytes,
            "postcap_bacteria": self.postcap_bacteria,
            "ph": self.ph,
            "dna_fragmentation": self.dna_fragmentation,
            "lab_comment": self.lab_comment,
            "user_id": self.user_id
        }

    
class Complaint(db.Model):
    __tablename__ = 'complaint'
    id = db.Column(db.Integer, primary_key=True)
    cause = db.Column(db.String(250), unique=False, nullable=False)
    url_image_complaint = db.Column(db.String, nullable=True)
    complaint_comment = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    latitude = db.Column(db.String(80), nullable=True)
    longitude = db.Column(db.String(80), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "cause": self.cause,
            "url_image_complaint": self.url_image_complaint,
            "complaint_comment": self.complaint_comment,
            "status": self.status,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "user_id": self.user_id
        }

    
