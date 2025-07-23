print("====== Smart Farm Task Organizew ======")
print("1. เพิ่มงานในฟาร์ม")
print("2. แสดงรายการงานทั้งหมด")
print("3. ลบงาน")
print("4. สรุปจำนวนงานในแต่ละประเภท")
print("5. ออกจากโปรแกรม")

task_list = []
while True:
    choice = input("เลือกเมนู (1-5): ")
    
    if choice == '1':
        taskname = input("ป้อนชื่องาน")
        date = input("ป้อนวันที่ (dd/mm/yyyy): ")
        genre = input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ")
        task_list.append({
            'taskname': taskname,
            'date': date,
            'genre': genre
        })
        print("เพิ่มงานสำเร็จ")
        
    elif choice == '2':
        print("รายการงานทั้งหมด")
        index = 1
        for task in task_list:
            print(f"{index}. {task['date']} - {task['taskname']} ({task['genre']})")
            index += 1
       
        elif choice == '3':
            print("รายการทั้งหมด")
            index = 1
            for task in task_list:
                print(f"{index}. {take['date']} - {task['takename']} ({take['genre']})")
                index += 1
            
            delete_index = int(input("ลำดับของงานที่ต้องการลบ: "))
            if 1<= delete_index <= len(task_list):
                delete_task = task_list.pop(delete_index - 1)
                print(f"ลบงาน: {delete_task['taskname']} แล้ว")

            elif choice == '14':
                print("สรุปจำนวนงานแต่ลล่ะประเภท")

                count_genre = {}

                for task in task_list:
                    genre = task['genre']
                    if genre in count_genre:
                        count_genre[genre] += 1 # มีแล้ว --> นับเพิ่ม
                    else:
                        count_genre[genre] = 1 # ยังไม่มี --> เริ่มนับ

                for genre, count in count_genre.items():
                    print(f"- {genre}: {count} งาน")

                elif choice == '5':
                    print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
                    break
