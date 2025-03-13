"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
  phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
  def count_summa(products_sold):
        sold_sum = 0
        for sold in products_sold:
            sold_sum += sold
        return sold_sum
  def count_average(products_sold):
        sold_sum = 0
        for sold in products_sold:
            sold_sum += sold
        sold_avg = sold_sum/len(products_sold)
        return sold_avg
  for one_product in phones:
        product_sold_sum = count_summa(one_product['items_sold'])
        print(f'Суммарное количество продаж для {one_product['product']}: {product_sold_sum}')
  for one_product in phones:
        product_sold_avg = count_average(one_product['items_sold'])
        print(f'Среднее количество продаж для {one_product['product']}: {product_sold_avg}')
  product_sold_sum = 0
  product_sold_avg = 0
  for one_product in phones:
        product_sold_sum += count_summa(one_product['items_sold'])
        product_sold_avg += count_summa(one_product['items_sold'])/len(phones)
  print(f'Суммарное количество продаж: {product_sold_sum}')
  print(f'Среднее количество продаж: {product_sold_avg}')

if __name__ == "__main__":
    main()
