def get_client_ip(request):
    # 'HTTP_X_FORWARDED_FOR'ヘッダを参照して転送経路のIPアドレスを取得する。
    forwarded_addresses = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_addresses:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがある場合: 転送経路の先頭要素を取得する。
        client_addr = forwarded_addresses.split(',')[0]
    else:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがない場合: 直接接続なので'REMOTE_ADDR'ヘッダを参照する。
        client_addr = request.META.get('REMOTE_ADDR')

    # 取得したアドレスをそのまま返す。
    return client_addr