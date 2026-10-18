

def test_page_timezone_reads_the_declared_zone_or_none():
    from custom_components.amazon_orders.account.pages import page_timezone

    assert page_timezone("<html></html>") is None
