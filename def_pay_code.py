def compute_pay():
    try:
         frate= float(rate)
         fhours= float(hours)
         if hours>40:
             xhours = (fhours-40)
             xrate = (frate *1.5)
             xpay = (40*frate)+(xhours*xrate)
         else:
             gpay =(frate*fhours)
