


def join(*l,  sep='-'):
    """
       This function is in charge of separate all the Cup_of_join
       """
    m_list = []

    if not l:
        return None

    for index in l:

        m_list += index
        m_list.append(sep)

    return m_list[:]


# ----------------------------------------------------------------------------------------------------------------------
def get_price(prices, optionals=[], **ingredients):
    """
   This function get ingredients and how much there is and is in charge of returning the price
   """
    total_sum = 0

    for i in ingredients:
        if i not in optionals:
            total_sum += prices[i] * ingredients.get(i)

    return total_sum//100
#returning the total sum after all the calculation
# ----------------------------------------------------------------------------------------------------------------------
