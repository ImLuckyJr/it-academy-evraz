# ИТ-академия ЕВРАЗа (web/frontend/2_css)

&nbsp;&nbsp;&nbsp;<a href="#css-base">1. CSS, основы.</a>

&nbsp;&nbsp;&nbsp;<a href="#css-selectors">2. CSS, селекторы</a>

&nbsp;&nbsp;&nbsp;<a href="#css-flexbox">3. CSS, flexbox.</a>

&nbsp;&nbsp;&nbsp;<a href="#css-margins">4. CSS, работа с отступами и с float.</a>

&nbsp;&nbsp;&nbsp;<a href="#css-margins">5. Практика, верстаем свои шаблоны.</a>

<!-- Начало блока 1 -->
<a style="dislay: none" id="css-base"></a>
## 1. CSS, основы[⬆](#contents)

> __Полезные ссылки__: [Все о CSS](https://html5book.ru/css-css3/), [Все свойства CSS](https://hcdev.ru/css/margin//)


<a style="dislay: none" id="base-html"></a>
### Задачи на выполнение базовых операций[⬆](#contents)

<details><summary>Показать / Скрыть</summary>
<p>

![1](https://user-images.githubusercontent.com/33654512/160240490-193c12de-2eed-44a1-97ed-1ef181e812ed.png)

![2](https://user-images.githubusercontent.com/33654512/160240495-74f9bd15-6138-443d-b1df-ab1c845b54f3.png)

![3](https://user-images.githubusercontent.com/33654512/160240501-8a582011-569f-4d1b-9991-3e6ee1e1620b.png)

![4](https://user-images.githubusercontent.com/33654512/160240523-94c6f25d-863f-4ff6-b6a3-03ffbce9e431.png)

![5](https://user-images.githubusercontent.com/33654512/160240536-fc0dfd06-ba42-4419-9ddb-dab4297b0455.png)

![6](https://user-images.githubusercontent.com/33654512/160240545-fc38f952-d509-4d34-b4bd-4285a3386b60.png)

![7](https://user-images.githubusercontent.com/33654512/160240548-2b02b1e3-2f4b-402e-b8e9-d8aeb50eca0e.png)

![8](https://user-images.githubusercontent.com/33654512/160240555-0d7e67a8-090d-416f-ab94-d2a55ea3b36a.png)

</p>
</details>

<!-- Начало блока 2 -->
<a style="dislay: none" id="css-selectors"></a>
## 2. CSS, селекторы[⬆](#contents)

> __Полезные ссылки__: [Все о CSS](https://html5book.ru/css-css3/), [Все свойства CSS](https://hcdev.ru/css/margin//)

Прежде чем начать изучать селекторы, знакомимся с новым написанием стилей.

### Внешняя таблица стилей

<details><summary>Показать / Скрыть</summary>
<p>

Внешняя таблица стилей представляет собой текстовый файл с расширением `.css`, в котором находится набор CSS-стилей элементов. Файл создаётся в редакторе кода, так же как и HTML-страница. Внутри файла могут содержатся только стили, без HTML-разметки. Внешняя таблица стилей подключается к веб-странице с помощью элемента `<link>`, расположенного внутри раздела `<head></head>`. Такие стили работают для всех страниц сайта.

К каждой веб-странице можно присоединить несколько таблиц стилей, добавляя последовательно несколько элементов `<link>`, указав в атрибуте media назначение данной таблицы стилей. `rel="stylesheet"` указывает тип ссылки (ссылка на таблицу стилей).

```HTML
<head>
    <link rel="stylesheet" href="css/style.css">
</head>
```

```CSS
/* Файл style.css */
html { height: 100%; }
body {
    width: 100%;
    height: 100%;
    background-color: red;
}
```

</p>
</details>

### Внутренние стили

<details><summary>Показать / Скрыть</summary>
<p>

Внутренние стили встраиваются в раздел `<head></head>` HTML-документа и определяются внутри элемента `<style></style>`. Внутренние стили имеют приоритет над внешними, но уступают встроенным стилям (заданным через атрибут `style`).

```HTML
<head>
    <style>
    h1, h2 {
        color: red;
        font-family: "Times New Roman", Georgia, Serif;
        line-height: 1.3em;
    }
    </style>
</head>
<body>
...
</body>
```

</p>
</details>


### Встроенные стили (то, как мы уже делали)

<details><summary>Показать / Скрыть</summary>
<p>

Когда мы пишем встроенные стили, мы пишем CSS-код в HTML-файл, непосредственно внутри элемента с помощью атрибута `style`. Такие стили действуют только на тот элемент, для которого они заданы.

```HTML
<p style="font-weight: bold; color: red;">Обратите внимание на этот текст.</p>
```

</p>
</details>

### ID и class атрибуты

<details><summary>Показать / Скрыть</summary>
<p>

**id** - Определяет уникальный идентификатор элемента. Его цель — идентифицировать элемент при связывании (используя идентификатор фрагмента — якорь), сценарии или стилизации с помощью CSS. Значение **id** не должно содержать пробелов. В отличие от атрибута class, элементы могут иметь только одно единственное значение идентификатора.

```HTML
<div id="content"> ... </div>
```

**class** - Представляет собой разделенный пробелом список классов элемента с учетом регистра. Классы позволяют CSS и Javascript выбирать и получать доступ к элементам с помощью селекторов классов или функций, таких как метод DOM.

```HTML
<div class="card">
    <div class="card-title text-red">Заголовок</p>
    <div class="card-body">Тело</p>
</div>

<div class="card">
    <div class="card-title text-red">Заголовок</p>
    <div class="card-body">Тело</p>
</div>
```

</p>
</details>

## Виды селекторов

Селекторы представляют структуру веб-страницы. С их помощью создаются правила для форматирования элементов веб-страницы. Селекторами могут быть элементы, их классы и идентификаторы, а также псевдоклассы и псевдоэлементы.

### Селектор элемента

<details><summary>Показать / Скрыть</summary>
<p>

Селекторы элементов позволяют форматировать все элементы данного типа на всех страницах сайта. Например, зададим общий стиль форматирования всех заголовков **h1**:
```CSS
h1 {font-family: Lobster, cursive;}
```

</p>
</details>

### Селектор класса

<details><summary>Показать / Скрыть</summary>
<p>

Селекторы класса позволяют задавать стили для одного и более элементов с одинаковым именем класса, размещенных в разных местах страницы или на разных страницах сайта. Например, для создания заголовка с классом `headline` необходимо добавить атрибут `class` со значением `headline` в открывающий тег `<h1>` и задать стиль для указанного класса. Стили, созданные с помощью класса, можно применять к другим элементам, не обязательно данного типа.

```HTML
<h1 class="headline">Инструкция пользования персональным компьютером</h1>
```

```CSS
.headline {
    text-transform: uppercase; 
    color: lightblue;
}
```

</p>
</details>

### Селектор идентификатора

<details><summary>Показать / Скрыть</summary>
<p>

Селектор идентификатора позволяет форматировать один конкретный элемент. Значение `id` должно быть уникальным, на одной странице может встречаться только один раз и должно содержать хотя бы один символ. Значение не должно содержать пробелов.

```HTML
<div id="sidebar"></div>
```

```CSS
#sidebar {
    width: 300px; 
    float: left;
}
```

</p>
</details>

### Селектор потомка

<details><summary>Показать / Скрыть</summary>
<p>

Селекторы потомков применяют стили к элементам, расположенным внутри элемента-контейнера. Например, `ul li {text-transform: uppercase;}` — выберет все элементы `li`, являющиеся потомками всех элементов `ul`.

Если нужно отформатировать потомки определенного элемента, этому элементу нужно задать стилевой класс:

- `p.first a {color: green;}` — данный стиль применится ко всем ссылкам, потомкам абзаца с классом `first`;
- `p .first a {color: green;}` — если добавить пробел, то будут стилизованы ссылки, расположенные внутри любого элемента класса `.first`, который является потомком элемента `<p>`;
- `.first a {color: green;}` — данный стиль применится к любой ссылке, расположенной внутри другого элемента, обозначенного классом `.first`.

</p>
</details>

### Селектор псевдокласса

<details><summary>Показать / Скрыть</summary>
<p>

Псевдоклассы — это классы, фактически не прикрепленные к HTML-элементам. Они позволяют применить CSS-правила к элементам при совершении события или подчиняющимся определенному правилу. Например, если мы хотим поменять фон блока при наведении:

```HTML
<div class="card"> ... </div>
```

```CSS
.card {
    width: 200px;
    height: 20px;
    background-color: red;
}
.card:hover {
    background-color: green;
}
```

</p>
</details>

### Группировка селекторов

<details><summary>Показать / Скрыть</summary>
<p>

Один и тот же стиль можно одновременно применить к нескольким элементам. Для этого необходимо в левой части объявления перечислить через запятую нужные селекторы:

```CSS
h1, 
h2, 
p, 
span {
    color: tomato; 
    background: white;
}
```

</p>
</details>

<a style="dislay: none" id="base-html"></a>
## Задачи на выполнение[⬆](#contents)

<details><summary>Показать / Скрыть</summary>
<p>

![1](https://user-images.githubusercontent.com/33654512/160240495-74f9bd15-6138-443d-b1df-ab1c845b54f3.png)

![2](https://user-images.githubusercontent.com/33654512/160240501-8a582011-569f-4d1b-9991-3e6ee1e1620b.png)

![3](https://user-images.githubusercontent.com/33654512/160240548-2b02b1e3-2f4b-402e-b8e9-d8aeb50eca0e.png)

![4](https://user-images.githubusercontent.com/33654512/162421979-8f00e7c8-ab2b-4399-b695-4d42b935b5d5.png)

![5](https://user-images.githubusercontent.com/33654512/162422333-78dd9fa2-60eb-4bca-a6d5-4740ae422cfd.png)

![6](https://user-images.githubusercontent.com/33654512/162421921-4518fec4-bf4a-45f1-97b1-e7a8e74243c8.png)

</p>
</details>

<!-- Начало блока 3 -->
<a style="dislay: none" id="css-flexbox"></a>
## 3. CSS, flexbox[⬆](#contents)

> __Полезные ссылки__: [Все о CSS](https://html5book.ru/css-css3/), [Шпаргалка по Flexbox](https://tpverstak.ru/flex-cheatsheet/), [Все свойства CSS](https://hcdev.ru/css/margin//)


<a style="dislay: none" id="base-html"></a>
### Задачи для выполнения[⬆](#contents)

<details><summary>Показать / Скрыть</summary>
<p>

![1](https://user-images.githubusercontent.com/33654512/161277827-6f0c2aa2-437e-421a-8f38-c1f662155900.png)

![2](https://user-images.githubusercontent.com/33654512/161277844-31b361a4-43b4-4552-ad69-8af2c44ed00d.png)

![3](https://user-images.githubusercontent.com/33654512/161277847-c3eb7007-c5ec-4a67-8b43-a35c03089e65.png)

![4](https://user-images.githubusercontent.com/33654512/161277851-555f3841-6c9a-4a10-9489-73802295d084.png)

![5](https://user-images.githubusercontent.com/33654512/161277855-c4d66d75-b3f9-46e4-b2e5-454b41e5b590.png)

![6](https://user-images.githubusercontent.com/33654512/161277862-1935891a-e699-4134-b56f-5305afea6b03.png)

![7](https://user-images.githubusercontent.com/33654512/161277869-4f5f00f5-3b7c-4ae8-a73c-72849d91f1d9.png)

![8](https://user-images.githubusercontent.com/33654512/161277874-d897a6ac-bae2-486d-8a8b-1392af4d6d08.png)

![10](https://user-images.githubusercontent.com/33654512/161277889-2571a74f-21b9-45d4-81c0-204b049f1ddf.png)

![11](https://user-images.githubusercontent.com/33654512/161277892-52db91d9-8b04-4a3a-9a83-3126b84c0386.png)

![12](https://user-images.githubusercontent.com/33654512/161277898-cff47a6a-789f-428d-a078-ae80386ded62.png)

![13](https://user-images.githubusercontent.com/33654512/161277909-3b07352f-c0cc-45a6-824c-b8d78f5ad2da.png)

![14](https://user-images.githubusercontent.com/33654512/161277916-769004c2-6888-4cb4-be5e-481e1bcc62be.png)

![15](https://user-images.githubusercontent.com/33654512/161277919-57a3dfb6-59fd-4c24-9051-96ac3f189844.png)

![16](https://user-images.githubusercontent.com/33654512/161277929-b77a92f6-67c9-4e71-855b-02d6c2216b05.png)

![17](https://user-images.githubusercontent.com/33654512/161277934-f0808741-b83b-47cb-8465-f32454bb8cdd.png)

![18](https://user-images.githubusercontent.com/33654512/161277940-d241c85a-e614-4f6e-bd59-dcb65bbb7bd0.png)

![20](https://user-images.githubusercontent.com/33654512/161277945-fb51c197-fe39-4f80-b6fc-0ac7589bc197.png)


</p>
</details>

<!-- Начало блока 4 -->
<a style="dislay: none" id="css-margins"></a>
## 4. CSS, свойства блоков [⬆](#contents)

> __Полезные ссылки__: [Все о CSS](https://html5book.ru/css-css3/), [Все свойства CSS](https://hcdev.ru/css/margin//)

![image](https://user-images.githubusercontent.com/33654512/162419318-477b9a52-fd44-4955-ba62-de66111e76e0.png)

### padding

> Основное предназначение **padding** — создать пустое пространство вокруг содержимого элемента, например текста, чтобы он не прилегал плотно к краю элемента. Использование **padding** повышает читабельность текста и улучшает внешний вид страницы.
>
> **padding**: все стороны; `(padding: 10px;)`
>
> **padding**: верх-низ лево-право; `(padding: 10px 20px;)`
>
> **padding**: верх лево-право низ; `(padding: 10px 20px 5px;)`
>
> **padding**: верх право низ лево; `(padding: 5px 10px 15px 20px;)`

### border

> Свойство **border** добавляет вокруг элемента рамку заданной толщины, стиля и цвета. Для создания линий на отдельных сторонах элемента используются свойства **border-top**, **border-right**, **border-bottom** и **border-left**, соответственно устанавливающие линию сверху, справа, снизу и слева. Так же эти свойства могут быть использованы и чтобы убрать линию на определённой стороне. Если свойство **padding** не задано, то рамка начинается сразу вокруг содержимого.
>
> **border**: 2px solid #0069b5; *Параметры рамки*
>
> **border-left**: none; *Убираем линию слева*
>
> **border-right**: none; *Убираем линию справа*
>
> Здесь имеет значение порядок свойств — сперва устанавливаем рамку, и лишь после этого убираем линии на нужных сторонах.

### margin

> Свойство **margin** устанавливает пустое пространство от внешнего края **border**, **padding** или содержимого блока (рис. 1). Под **margin** нет своего фона и он принимает фон родительского элемента. **margin** в основном используется для создания вертикальных и горизонтальных отступов между элементами. Аналогично другим блочным свойствам есть свойства для каждой стороны — **margin-top**, **margin-right**, **margin-bottom** и **margin-left**, соответственно устанавливающие отступ сверху, справа, снизу и слева.
>
> **margin**: все стороны; `(margin: 10px;)`
>
> **margin**: верх-низ лево-право; `(margin: 10px 20px;)`
>
> **margin**: верх лево-право низ; `(margin: 10px 20px 5px;)`
>
> **margin**: верх право низ лево; `(margin: 5px 10px 15px 20px;)`
>
> **margin** может быть задан с отрицательным значением, тем самым элемент сдвигается в противоположном направлении. К примеру, **margin-top**:-10px поднимает блок вверх на 10 пикселей, а **margin-left**:-10px сдвигает блок влево.

<a style="dislay: none" id="base-html"></a>
### Схлопывание margin[⬆](#contents)

<details><summary>Показать / Скрыть</summary>
<p>
> Если оба значения margin положительные, то из них выбирается наибольшее значение и оно задаётся как расстояние между блоков.    

![image](https://user-images.githubusercontent.com/33654512/162418153-7dd28e2b-6060-4230-9496-68066260318b.png)

> Если один из margin отрицательный, тогда margin вычитаются.

![image](https://user-images.githubusercontent.com/33654512/162418248-d9c29176-e52a-4d2d-a6ab-2a61901f9a20.png)

> Если оба margin отрицательные, то из двух значений выбирается наибольшее по модулю, оно же и выступает в качестве отрицательного отступа между элементами.

![image](https://user-images.githubusercontent.com/33654512/162418526-bb919e92-7bee-4327-9bd9-8bf553269d6a.png)

</p>
</details>

<a style="dislay: none" id="base-html"></a>
### Задачи для выполнения[⬆](#contents)

<details><summary>Показать / Скрыть</summary>
<p>

![image](https://user-images.githubusercontent.com/33654512/162421818-b143cb3b-1910-4740-a2d8-1e27c3b32856.png)

![image](https://user-images.githubusercontent.com/33654512/162421879-c2757892-c205-4572-8624-9818714bacbb.png)

![image](https://user-images.githubusercontent.com/33654512/162421902-07df7ff0-4f13-4818-bc85-17e7fb880079.png)

![image](https://user-images.githubusercontent.com/33654512/162421921-4518fec4-bf4a-45f1-97b1-e7a8e74243c8.png)

![image](https://user-images.githubusercontent.com/33654512/162422190-5e9e469b-29b5-4411-9e33-5c8c6918d7e3.png)

![image](https://user-images.githubusercontent.com/33654512/162422333-78dd9fa2-60eb-4bca-a6d5-4740ae422cfd.png)

![image](https://user-images.githubusercontent.com/33654512/162421936-de3c9c72-f82f-4aba-b126-0cdb1916e7c1.png)

![image](https://user-images.githubusercontent.com/33654512/162422615-3ad82774-ed23-4d2b-b7dc-2ae7370f2137.png)

![image](https://user-images.githubusercontent.com/33654512/162421979-8f00e7c8-ab2b-4399-b695-4d42b935b5d5.png)

![image](https://user-images.githubusercontent.com/33654512/162422025-238bfac3-19b0-47ec-9d1e-759af5406d72.png)

![image](https://user-images.githubusercontent.com/33654512/162422050-ffd1ad0d-4006-4098-abd3-eccdf3b3ef6a.png)


</p>
</details>

<!-- Начало блока 5 -->
<a style="dislay: none" id="css-base"></a>
## 1. Практика, верстаем свои шаблоны[⬆](#contents)

[Шаблон 1](http://psd-html-css.ru/sites/default/files/public/old/demo/psd-html-css.ru-Metronic_Aironepage_FrontendFreebie.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488858/1.zip)

[Шаблон 2](http://psd-html-css.ru/sites/default/files/public/old/demo/king-template.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488861/2.zip)

[Шаблон 3](http://psd-html-css.ru/sites/default/files/public/old/demo/FireShotCaptureGuriGuriNyoiBootstrap.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488864/3.zip)

[Шаблон 4](http://psd-html-css.ru/sites/default/files/public/old/demo/FireShotCaptureLand.io.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488867/4.zip)

[Шаблон 5](http://psd-html-css.ru/sites/default/files/public/old/demo/FireShotCaptureActiveBox.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488868/5.zip)

[Шаблон 6](http://psd-html-css.ru/sites/default/files/public/old/demo/CaptureHalcyonDays.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488869/6.zip)

[Шаблон 7](http://psd-html-css.ru/sites/default/files/public/old/demo/FireShotCaptureTheBloomWebsiteTemplate.jpg), [архив с картинками](https://github.com/ImLuckyJr/it-academy-evraz/files/8488870/7.zip)
