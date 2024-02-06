import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    """
    Login Table
    link: https://www.testdome.com/questions/python-data-science/login-table/81252
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.   
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                                    is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place. 
                    It should not return anything.
    """   
    pw=[]
    for i in id_password:
        pw.append(i[1])
    id_name_verified['Password']=pw
    id_name_verified.drop(labels=['Verified'], axis=1, inplace=True)
    return 

id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)