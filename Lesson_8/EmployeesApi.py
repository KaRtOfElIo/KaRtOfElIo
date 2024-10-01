import requests


class WorkersApi:  # Приведем название класса к стандарту (с заглавной буквы)
    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        resp.raise_for_status()  # Проверка на успешный запрос
        return resp.json().get('userToken')

    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        headers = {"x-client-token": self.get_token()}
        resp = requests.post(f"{self.url}/company", json=company, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def get_company(self, company_id):
        resp = requests.get(f"{self.url}/company/{company_id}")
        resp.raise_for_status()
        return resp.json()

    def get_employee(self, employee_id):
        resp = requests.get(f"{self.url}/employee/{employee_id}")
        resp.raise_for_status()
        return resp.json()

    def get_employees_list(self, company_id):
        params = {'company': company_id}
        resp = requests.get(f"{self.url}/employee", params=params)
        resp.raise_for_status()
        return resp.json()

    def create_employee(self, first_name, last_name, middle_name, company_id, email, url, phone, birthdate,
                        is_active=True):
        employee = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active
        }
        headers = {"x-client-token": self.get_token()}
        resp = requests.post(f"{self.url}/employee", json=employee, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def edit_employee(self, employee_id, last_name=None, email=None, url=None, phone=None, is_active=None):
        employee_data = {}
        if last_name:
            employee_data["lastName"] = last_name
        if email:
            employee_data["email"] = email
        if url:
            employee_data["url"] = url
        if phone:
            employee_data["phone"] = phone
        if is_active is not None:
            employee_data["isActive"] = is_active

        headers = {"x-client-token": self.get_token()}
        resp = requests.patch(f"{self.url}/employee/{employee_id}", json=employee_data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def delete_employee(self, employee_id):
        headers = {"x-client-token": self.get_token()}
        resp = requests.delete(f"{self.url}/employee/{employee_id}", headers=headers)
        resp.raise_for_status()
        return resp.json()
