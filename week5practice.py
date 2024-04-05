class Student:

    def __init__(self, Kscore, Escore, Mscore):
        self.Kscore = Kscore
        self.Escore = Escore
        self.Mscore = Mscore
    def average(self):
        return (self.Kscore+self.Escore+self.Mscore)/3

Snum = int(input('학생 수 입력 (N): '))
for i in range(Snum):
    Kscore = float(input(f'{i+1}번째 학생의 국어 성적 입력: '))
    Escore = float(input(f'{i+1}번째 학생의 영어 성적 입력: '))
    Mscore = float(input(f'{i+1}번째 학생의 수학 성적 입력: '))
    student=Student(Kscore, Escore, Mscore)
    avg=student.average()
    print(f'{i+1}번째 학생의 평균 점수: {avg}')