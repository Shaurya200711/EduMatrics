import data_store
import analytics_engine

def dbr(value):
    blocks = int(value)
    return "█" * blocks

def main():
    tu = set()
    
    while True:
        print("\n=== VIT ACADEMIC FORECASTER ===")
        print("1. CGPA Forecaster")
        print("2. Attendance Forecaster")
        print("3. Exit Program")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "3":
            print("Exiting...")
            break
            
        if choice in ["1", "2"]:
            reg_no = input("\nEnter Registration Number: ").upper()
            tu.add(reg_no)
            
            student = data_store.rec.get(reg_no)
            if not student:
                print("\n>>> Student not found in database. Let's register them.")
                name = input("Enter Student Name: ")
                branch = input("Enter Branch (e.g., CSE_CORE): ")
                creds = int(input("Enter completed credits (e.g., 20 for 1st Year): "))
                cgpa = float(input("Enter current CGPA: "))
                
                data_store.rec[reg_no] = {
                    "name": name,
                    "branch": branch,
                    "com_cred": creds,
                    "curr_cgpa": cgpa
                }
                student = data_store.rec[reg_no]
                print(f">>> Profile for {name} successfully created in active memory.")
            
            print(f"\n--- PROFILE: {student['name']} ({student['branch']}) ---")
            print(f"Current CGPA: {student['curr_cgpa']} | Credits: {student['com_cred']}")
            
            if choice == "1":
                target = float(input("Enter Target CGPA: "))
                print("\nA. Immediate Next Semester")
                print("B. Long-Term Degree Forecast")
                sub_choice = input("Select mode (A/B): ").upper()
                
                if sub_choice == "A":
                    credits_next = int(input("Enter credits for next semester (e.g., 20): "))
                    required_val, status = analytics_engine.req_sgpa(reg_no, target, credits_next)
                    
                    print(f"\n--- FORECAST RESULT ---")
                    print(f"Required SGPA: {required_val} ({status})")
                    print(f"Current : {student['curr_cgpa']} |{dbr(student['curr_cgpa'])} |")
                    if 0 < required_val <= 10.0:
                        print(f"Target  : {required_val} |{dbr(required_val)} |")
                        
                elif sub_choice == "B":
                    rem_sems = int(input("Enter remaining semesters (e.g., 7): "))
                    rem_credits = int(input("Enter total remaining credits to graduate: "))
                    
                    required_val, status = analytics_engine.req_sgpa(reg_no, target, rem_credits)
                    
                    print(f"\n--- LONG-TERM TIMELINE ---")
                    print(f"Sustained SGPA needed across {rem_sems} semesters: {required_val} ({status})")
                    print(f"Current  : {student['curr_cgpa']} |{dbr(student['curr_cgpa'])} |")
                    if 0 < required_val <= 10.0:
                        for i in range(1, rem_sems + 1):
                            print(f"Future S{i}: {required_val} |{dbr(required_val)} |")
            
            elif choice == "2":
                print("\n(Attendance Evaluation)")
                attended = int(input("Enter number of classes attended: "))
                total = int(input("Enter total number of classes held: "))
                
                percent, count, action = analytics_engine.check_atten(attended, total)
                print(f"\n--- ATTENDANCE REPORT ---")
                print(f"Current Percentage: {percent}%")
                print(f"Action: {action} ({count} classes)")

if __name__ == "__main__":
    main()