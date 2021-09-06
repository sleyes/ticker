from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.shortcuts import render
import requests, logging

class GetTicker(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        logger = logging.getLogger()
        logger.info(1, 'GetTicker %s', 'args', extra={'userid': request.user.id})
        
        symbol = request.GET.get('symbol', None)
        if not symbol:
            return Response({'error': 'symbol is required'})
        
        r = requests.get('https://www.alphavantage.co/query', params={'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'outputsize': 'compact', 'apikey': 'X86NOH6II01P7R24'})
        
        data = r.json()
        if 'Meta Data' not in data or 'Time Series (Daily)' not in data:
            return Response({'error': data['Error Message'] if 'Error Message' in data else data})
        
        time_series = data['Time Series (Daily)']
        if len(time_series) < 2:
            return Response({'error': 'insuficient data returned'})
        
        dates = [x for x in time_series.keys()]
        dates.sort(reverse=True)
        o = time_series[dates[0]]['1. open']
        h = time_series[dates[0]]['2. high']
        l = time_series[dates[0]]['3. low']
        c0 = float(time_series[dates[0]]['4. close'])
        c1 = float(time_series[dates[1]]['4. close'])
        v = "{v:08.4f}".format(v=c0 - c1)
        
        return Response({'symbol': symbol,
                         'open_price': o,
                         'higher_price': h,
                         'lower_price': l,
                         'variation_between_last_2_closing_prices': v,
                         })