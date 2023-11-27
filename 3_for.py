"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
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
sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]       

def count_sum_sold(items_sold):
  sum_sold = 0
  for item in items_sold:
    sum_sold += item
  return sum_sold      

def sum_product_sales(products_sales):
  for one_product in products_sales:
     one_product['sum_sold'] = count_sum_sold(one_product['items_sold'])
     
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_product_sales(sales)
    sum_all_sales = 0
    count_all_sales = 0

    for sale in sales:
       sum_all_sales += sale['sum_sold']
       print(f"суммарное количество продаж {sale['product']} - {sale['sum_sold']} шт")
      
    for sale in sales:
       count_sales = len(sale['items_sold'])
       count_all_sales += count_sales
       if count_sales == 0:
          avg_sale = 0
       else:
          avg_sale = round(sale['sum_sold']/count_sales, 2)
       print(f"среднее количество продаж {sale['product']} - {avg_sale}")

    print(f"суммарное количество продаж всех товаров - {sum_all_sales}")      
   
    if count_all_sales == 0:
      avg_all_sales = 0
    else:
      avg_all_sales = round(sum_all_sales/count_all_sales, 2)   
    print(f"среднее количество продаж всех товаров - {avg_all_sales}")

if __name__ == "__main__":
    main()
