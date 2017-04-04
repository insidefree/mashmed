from Assuta.Assuta import Assuta
from Models.Person.Doctor import Doctor


class AssutaOld(Assuta):
    def __init__(self):
        Assuta.__init__(self)

    def save_doctors(self):
        self.driver.get('http://assuta-hospital.com/nashi-vrachi.aspx')
        links2 = [link.get_attribute('href') for link in
                  self.driver.find_elements_by_xpath("//ul[@class='doctorSlider_list js-doctorSlider_list']/li/a")]
        ent_flag = True
        ophthalmologist_flag = True
        surgeon_flag = True
        uro_gynecology_flag = True
        for link in links2:
            # print('{}'.format(link))
            self.driver.get(link)
            name = self.driver.find_element_by_xpath('//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/'
                                                     'table/tbody/tr/td[2]/div[2]/div/div/h1')
            # print('* ', name.text)

            if name.text == 'ЛОР-СПЕЦИАЛИСТЫ' and ent_flag is True:
                ent_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/p')]
                AssutaOld.save_doctors_from_sublist(ent_list[1::])
                ent_flag = False

            if name.text == 'НАШИ ОФТАЛЬМОЛОГИ' and ophthalmologist_flag is True:
                ophthalmologist_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/div[2]/p')]
                AssutaOld.save_doctors_from_sublist(ophthalmologist_list)
                ophthalmologist_flag = False

            if name.text == 'ПЛАСТИЧЕСКИЕ ХИРУРГИ' and surgeon_flag is True:
                surgeon_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/div[2]/p')]
                AssutaOld.save_doctors_from_sublist(AssutaOld.handling_surgeon_list(surgeon_list, 'Подробнее >>'))
                surgeon_flag = False

            if name.text == 'УРОГИНЕКОЛОГИ' and uro_gynecology_flag is True:
                uro_gynecology_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/p')]
                AssutaOld.save_doctors_from_sublist(uro_gynecology_list[1::])
                uro_gynecology_flag = False
            if name.text != 'ЛОР-СПЕЦИАЛИСТЫ' and name.text != 'НАШИ ОФТАЛЬМОЛОГИ' \
                    and name.text != 'ПЛАСТИЧЕСКИЕ ХИРУРГИ' and name.text != 'УРОГИНЕКОЛОГИ':
                doctor = Doctor(name=name.text, birthday='', vacation='', image='', language='', info='', department='',
                                subDepartment='', visible_tg='', status='', first_tg='', link='')
            doctor.save()

    @staticmethod
    def save_doctors_from_sublist(doctors_list):
        for doctor in doctors_list[::2]:
            index = doctors_list.index(doctor)
            doctor = Doctor(name=doctor, birthday='', vacation='', image='', language='', info=doctors_list[index + 1],
                            department='', subDepartment='', visible_tg='', status='', first_tg='', link='')
            doctor.save()

    @staticmethod
    def handling_surgeon_list(lst, value):
        index = [ind for ind, el in enumerate(lst) if el == value]
        for ind in index[::-1]:
            del lst[ind]
            del lst[ind - 1]
            del lst[ind - 2]
        return lst
