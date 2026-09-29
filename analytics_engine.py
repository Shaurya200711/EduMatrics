import data_store
import math

def req_sgpa(reg_no, target_cgpa, fut_cred):
    student = data_store.rec.get(reg_no)
    if not student:
        return 0.0, "Not Found"
        
    curr_cgpa = student["curr_cgpa"]
    cred_earned = student["com_cred"]
    
    curr_points = curr_cgpa * cred_earned
    tot_tar_cred = cred_earned + fut_cred
    tar_points = target_cgpa * tot_tar_cred
    
    req_points = tar_points - curr_points
    
    if fut_cred == 0:
        return 0.0, "Invalid Credits"
        
    required = round(req_points / fut_cred, 2)
    
    if required > 10.0:
        return required, "Impossible"
    elif required <= 0.0:
        return 0.0, "Secured"
    else:
        return required, "Achievable"

def check_atten(attended, total):
    if total == 0:
        return 0.0, 0, "No classes held"
        
    curr_per = (attended / total) * 100
    
    if curr_per >= 75.0:
        buff_class = math.floor((attended - 0.75 * total) / 0.75)
        return round(curr_per, 2), buff_class, "Safe to miss"
    else:
        req_class = math.ceil((0.75 * total - attended) / 0.25)
        return round(curr_per, 2), req_class, "Must attend consecutively"