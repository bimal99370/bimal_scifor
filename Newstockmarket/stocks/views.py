from django.http import JsonResponse
import requests


def get_real_time_quotes(request, symbol):
    api_key = 'OEDJDXHATRLVCXHG'
    function = 'GLOBAL_QUOTE'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch real-time quotes'}, status=500)


def get_historical_data(request, symbol):
    api_key = 'OEDJDXHATRLVCXHG'
    function = 'TIME_SERIES_DAILY'
    outputsize = 'compact'  # Adjust as needed
    datatype = 'json'  # Adjust as needed
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&datatype={datatype}&apikey={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch historical data'}, status=500)


def get_company_info(request, symbol):
    api_key = 'OEDJDXHATRLVCXHG'
    function = 'OVERVIEW'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch company information'}, status=500)


def get_intraday_data(request):
    symbol = request.GET.get('symbol')
    interval = request.GET.get('interval', '5min')  # Default to 5-minute interval if not provided

    if symbol:
        api_key = 'OEDJDXHATRLVCXHG'
        function = 'TIME_SERIES_INTRADAY'
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Failed to fetch intraday data'}, status=500)
    else:
        return JsonResponse({'error': 'Symbol not provided'}, status=400)
