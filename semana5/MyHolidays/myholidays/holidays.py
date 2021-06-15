from datetime import date,datetime

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.holidays = []
        self._add_datas(args)

            
    def _valida_datas(self, *dts):
        data = False
        for dt in dts:
            if isinstance(dt, str):
                    try:
                        data = datetime.strptime(dt,'%d/%m/%Y').date()
                    except ValueError:
                        pass
            if isinstance(dt, date):
                data = dt
            return data
    
    def _add_datas(self, *args):
        for argument in args:
            if not isinstance(argument, tuple):
                argument = tuple(argument)
            for item in argument:
                formated_date = self._valida_datas(item)
                if formated_date:
                    self.datas.append(formated_date)


    def add_holiday(self, *dates):
        for argument in dates:
            formated_date = self._valida_datas(argument)
            if not formated_date:
                continue
            self.holidays.append(formated_date)
            if formated_date  not in self.datas:
                self.datas.append(formated_date)  
 
            
                
        
    def check_holiday(self,holiday):
        print(self.holidays)
        result = self._valida_datas(holiday)
        if result in self.holidays:
            return True
        else:
            return False
