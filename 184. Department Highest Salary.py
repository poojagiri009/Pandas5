import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salaryDictionary = {}
    for i in range(len(employee)):
        salary = employee['salary'][i]
        d_id = employee['departmentId'][i]
        if d_id in salaryDictionary:
            if salary > salaryDictionary[d_id]:
                salaryDictionary[d_id] = salary
        else:
            salaryDictionary[d_id] = salary
    deptDictionary = {}
    for i in range(len(department)):
        d_id=department['id'][i]
        d_name = department['name'][i]
        deptDictionary[d_id]=d_name
    result = []
    for i in range(len(employee)):
        d_id = employee['departmentId'][i]
        name = employee['name'][i]
        e_salary = employee['salary'][i]
        print(salaryDictionary)
        if salaryDictionary[d_id] == e_salary:
            result.append([d_id,name,e_salary]) 
    for element in result:
        d_id = element[0]
        element[0] = deptDictionary[d_id]

    return pd.DataFrame(result,columns=['Department','Employee','Salary'])

                
       
	
# Using pandas

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId',right_on='id',how='left')
    max_sal = df.groupby('name_y')['salary'].transform('max')
    df = df[df['salary'] == max_sal]
    return df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee'})