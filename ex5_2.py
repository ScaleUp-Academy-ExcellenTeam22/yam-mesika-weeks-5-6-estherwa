
def join(*l, sep: str ='-'):
    """
    This function is in charge of separate a list given by the program , the lenth of the list is undefined and this
    list will get combined with the separator
    @:param *l: we are getting the list here
    @:param separator: a separator that divides each list
    :return: we return the lists with the separator and without the last character
    """
    if not l:
        return None

    m_list = [list_cell for present_list in l for list_cell in present_list + [sep]]
    return m_list[:-1]

# ----------------------------------------------------------------------------------------------------------------------
def get_price(prices, optionals=[], **ingredients):
    """
   This function get ingredients and how much there meaning the amount in grams is and is in charge of returning the
   total price in order to be able to cook the recipe tact we desire
   :param prices : prices of 100 grams
   :param optionals: the list of the ingredients that are optional
   :param ingredients: the amaunt that we need to be able to cook the recipe
   :return: the total sum needed
   """
    total_sum = 0
    for i in ingredients:
        if i not in optionals:
            total_sum += prices[i] * ingredients.get(i)

    return total_sum // 100
# ----------------------------------------------------------------------------------------------------------------------

