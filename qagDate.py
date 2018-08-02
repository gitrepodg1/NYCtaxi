#qagDate.py  v1.3   20151108
#qagDate.py  v1.4   20151118


import datetime


class qagDateUtil():


    @classmethod
    def IsValidDateString(self, in_date, in_strformat="%Y%m%d"):

        try:
            ff=self.ConvertDateFormat(in_date,"String","Ordinal",in_strformat)
            return True
        except:
            return False


    @classmethod
    def ConvertDateToString(self,in_date):
        if type(in_date) is str:
            return in_date
        elif type(in_date) is int:
            return datetime.date.fromordinal(in_date).strftime('%Y%m%d')
        else:
            return "Error: Date must be YYYYMMDD string or Ordinal in ConvertDateToString" 


    @classmethod
    def ConvertDateToOrdinal(self, in_date):
        if type(in_date) is str:
            thedate = datetime.datetime.strptime(in_date, "%Y%m%d")
            return thedate.toordinal()
        elif type(in_date) is int:
            return in_date
        else:
            return "Error: Date must be YYYYMMDD string or Ordinal in ConvertDateToOrdinal" 


    def excel_date(self,date1):           #DateTime to Excel date (serial)
        temp = datetime.datetime(1899, 12, 31)
        delta = date1 - temp
        return float(delta.days) + (float(delta.seconds) / 86400) +1.0


    def float2datetime(self,serial):
        seconds = (serial - 25569) * 86400.0
        return datetime.datetime.utcfromtimestamp(seconds)


    def numpyfloat2datetime(self,numpyserial):
        return self.float2datetime(numpyserial-693594.0)




    @classmethod
    def ConvertDateFormat(self, in_date, in_type, out_type, in_strformat="%Y%m%d", out_strformat="%Y%m%d"):
    #ordinal: 1 January 0001 has ordinal value of 1
        if in_type is 'String':
            thedate = datetime.datetime.strptime(in_date, in_strformat) #convert string to datetime
            ordval =  thedate.toordinal()                               #convert datetime to ordinal
        elif in_type is 'Ordinal':
            ordval = in_date
        elif  in_type is 'DateTime':
            ordval = in_date.toordinal()  
        elif  in_type is 'Javascript':
            ordval = in_date / (24.0 * 3600000.0) + 719163.0  
        else:
            return "Error: invalid in_type in ConvertDateFormat"

        if out_type is 'String':
            outdate = datetime.date.fromordinal(ordval).strftime(out_strformat) 
        elif out_type is 'Ordinal':
            outdate = ordval
        elif out_type is 'Excel':
            ordDateTime = datetime.datetime.fromordinal(ordval)
            temp = datetime.datetime(1899, 12, 31)
            delta = ordDateTime - temp
            outdate =  float(delta.days) + (float(delta.seconds) / 86400) +1.0
        elif out_type is 'DateTime':
            outdate = datetime.datetime.fromordinal(ordval)
        elif out_type is 'Javascript':
            outdate = (ordval - 719163.0) * 24 * 3600000 
        else:
            return "Error: invalid out_type in ConvertDateFormat"

        return outdate


    @classmethod
    def ConvertDateFormatShifter(self, in_date, in_type, out_type, in_strformat="%Y%m%d", out_strformat="%Y%m%d", shiftNum=0, shiftUnit="d"):
    #ordinal: 1 January 0001 has ordinal value of 1
        if in_type is 'String':
            thedate = datetime.datetime.strptime(in_date, in_strformat) #convert string to datetime
            ordval =  thedate.toordinal()                               #convert datetime to ordinal
        elif in_type is 'Ordinal':
            ordval = in_date
        elif  in_type is 'DateTime':
            ordval = in_date.toordinal()  
        else:
            return "Error: invalid in_type in ConvertDateFormat"

        if shiftNum is not 0:
            if shiftUnit is "d":    
                ordval = ordval + shiftNum
            elif shiftUnit is "w":    
                ordval = ordval + shiftNum*7
                
        if out_type is 'String':
            outdate = datetime.date.fromordinal(ordval).strftime(out_strformat) 
        elif out_type is 'Ordinal':
            outdate = ordval
        elif out_type is 'Excel':
            ordDateTime = datetime.datetime.fromordinal(ordval)
            temp = datetime.datetime(1899, 12, 31)
            delta = ordDateTime - temp
            outdate =  float(delta.days) + (float(delta.seconds) / 86400) +1.0
        elif out_type is 'DateTime':
            outdate = datetime.datetime.fromordinal(ordval)
        elif out_type is 'Javascript':
            outdate = (ordval - 719163.0) * 24 * 3600000 
        else:
            return "Error: invalid out_type in ConvertDateFormat"

        return outdate

   


    
    @classmethod
    def ConvertDateFormatList(self, in_dateList, in_type, out_type, in_strformat="%Y%m%d", out_strformat="%Y%m%d"):
        n = len(in_dateList)
        return map(self.ConvertDateFormat,in_dateList,[in_type]*n, [out_type]*n, [in_strformat]*n, [out_strformat]*n)




