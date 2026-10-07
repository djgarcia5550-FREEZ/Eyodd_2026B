#creando una lista de estudiantes 
student_list_01 = [´jordan´,´pipen´,´curry´,´shack´]
student_list_02 = [´mike´,´saul´,´walter´,´jessy´]

#verificando presencia del estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student==student:
            print("Estudiante encontrado")
            return student
    #Si no encuentro al estudiante 
    print("Estudiante no encontrado")
    return None 

 #Probando algoritmo
 check_student("walter", student_list_01)           
 