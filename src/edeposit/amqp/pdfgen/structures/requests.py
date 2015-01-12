#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from collections import namedtuple, OrderedDict


# Functions & classes =========================================================
class GenerateContract(namedtuple("GenerateContract", ["firma",
                                                       "pravni_forma",
                                                       "sidlo",
                                                       "ic",
                                                       "dic",
                                                       "zastoupen",
                                                       "jednajici"])):
    pass


review = OrderedDict(
    nazev="Název ePublikace",
    podnazev="Podnázev",
    cast="Část (svazek,díl)",
    nazev_casti="Název části, dílu",
    isbn="ISBN (pokud je)",
    isbn_souboru_publikaci="ISBN souboru (pro vícesvazkové dokumenty)",
    generated_isbn='Přidělit agenturou ISBN',
    author1="Autor",
    author2="Autor 2",
    author3="Autor 3",
    poradi_vydani='Pořadí vydání, verze',
    misto_vydani='Místo vydání',
    rok_vydani="Rok vydání",
    nakladatel_vydavatel="Nakladatel",
    vydano_v_koedici_s='Vydáno v koedici s',
    cena='Cena v Kč',
    offer_to_riv='Zpřístupnit pro RIV',
    category_for_riv="Kategorie pro RIV",
    is_public='ePublikace je veřejná',
    libraries_accessing="Oprávnění knihovnám",
    libraries_that_can_access="Knihovny s přístupem k ePublikaci",
    zpracovatel_zaznamu='Zpracovatel záznamu',
    url="URL",
    file="Připojit soubor s ePublikací",
    format="Format of a file."
)


class GenerateReview(namedtuple("GenerateReview", list(review.iterkeys()))):
    pass


class RST2PDF(namedtuple("RST2PDF", ["rst_content",
                                     "style",
                                     "header",
                                     "footer"])):
    pass
