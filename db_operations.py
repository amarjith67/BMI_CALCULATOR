import cx_Oracle 

class bmi_db:
    def __init__(self,username,pass_word):
        self.conn=cx_Oracle.connect(user=username,password=pass_word,dsn="localhost/xe")
        self.cursor=self.conn.cursor()
        print("connected")
        
    def insert_data(self,user_id,name,age,height,weight):
        self.cursor.execute(f"INSERT INTO BMI VALUES({user_id},'{name}',{age},{weight},{height},NULL)")  
        self.bmi=(float(weight)/(float(height)*float(height)))*10000
        self.cursor.execute(f"UPDATE BMI SET BMI_VAL={self.bmi} WHERE ID={user_id}")
        if(self.bmi<18.5):
            self.message="Underweight"
        elif self.bmi >= 18.5 and self.bmi <= 24.9 :
             self.message="Normal"
        elif self.bmi >= 25.0 and self.bmi <= 29.9 :
             self.message="OverWeight" 
        elif self.bmi >= 30:
           self.message="Obese" 
        self.conn.commit()
        return self.bmi,self.message 
    
    def view_data(self,user_id,name):
        self.data=self.cursor.execute(f"SELECT * FROM BMI WHERE ID={user_id} AND NAME='{name}'")    
        self.conn.commit()
        return self.cursor
    
    def update_data(self,user_id,name,age,height,weight):
        self.bmi=(float(weight)/(float(height)*float(height)))*10000
        self.cursor.execute(f"UPDATE BMI SET NAME='{name}',AGE={age},WEIGHT={weight},HEIGHT={height},BMI_VAL={self.bmi} WHERE  ID={user_id}")
        self.conn.commit()
        return self.cursor
        