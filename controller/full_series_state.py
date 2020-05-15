import requests
import datetime
class FullSeriesState():
    def loadData(self, str_initial_date, str_last_date, uf):
        initial_date = datetime.datetime.strptime(str_initial_date,'%Y-%m-%d')
        last_date = datetime.datetime.strptime(str_last_date,'%Y-%m-%d')

        dates = self.get_dates(initial_date, last_date)

        #print(self.getState(dates, uf))
        return self.getState(dates, uf)

    def get_dates(self, initial_date, last_date):
        one_day = 86400
        initial_date_timestamp = initial_date.timestamp()
        last_date_timestamp = last_date.timestamp()
        dates = []
        while(initial_date_timestamp <= last_date_timestamp):
            dates.append(initial_date_timestamp)
            initial_date_timestamp += one_day
        return dates
    
    def getState(self, dates, uf):
        state = []
        for timestamp in dates:
            date = datetime.datetime.fromtimestamp(timestamp)
            day = f'0{date.day}' if date.day < 10 else date.day
            month = f'0{date.month}' if date.month < 10 else date.month
            string_date = f'{date.year}{month}{day}'

            response = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/{string_date}')
            if(response.ok):
                for data_state in response.json()['data']:
                    if data_state['uf'] == uf:
                        state.append(data_state)
        return state
