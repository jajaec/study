큰 제목 : 문서 제목
==========

작은 제목 : 문서 부제목
----------

# 글 머리 H1
## 글 머리 H2
### 글 머리 H2
#### 글 머리 H4
##### 글 머리 H5
###### 글 머리 H6

> This is a first blockqute.
>> This is a second blockqute.
>>> This is a third blockqute.

* 순서있는 목록 (번호 / 숫자는 의미없음 어떤 번호를 입력해도 순서는 내림차순으로 정의)

1. 첫번째
2. 두번째
3. 8번째

* 순서없는 목록 (글머리: *, +, - 지원 / 선호하는 방식으로 알아서 사용하면 됨.)

* 빨강
    * 녹색
        * 노랑


* 들여쓰기

This is a normal paragraph:
    
    This is a code block.

end code block.

* 코드블럭 코드 1

<pre><code>
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
</code></pre>

* 코드블럭 코드 2

```html
<a href="https://www.google.co.kr/" target="_blank">GOOGLE</a>
```

```css
.list > li {
  position: absolute;
  top: 40px;
}
```

```javascript
function func() {
  var a = 'AAA';
  return a;
}
```

```bash
$ vim ./~zshrc
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting. 
But let's throw in a tag.
```

* 인라인(inline) 코드 강조   
`background`혹은 `background-image` 속성으로 요소에 배경 이미지를 삽입할 수 있습니다.

* 수평선

***

---

* 링크

[link keyword][id]

[id]: URL "Optional Title here"

// code

Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"

* 외부링크

사용문법: [Title](link)

적용예: [Google](https://google.com/ "google link")

* 자동연결

외부링크: <http://example.com/>

이메일링크: <address@example.com>

* 강조

*single asterisks*   
_single underscores_

**double asterisks**

__double underscores__

~~cancelline~~


<img src="/path/to/img.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
<img src="/path/to/img.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

* 줄바꿈  
글 마지막에 3칸 이상 띄어쓰기(   )를 하면 줄이 바뀐다.

* 표(table)   

| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 |  |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 |  |
| `fixed` | 브라우저 창을 기준으로 배치 |  |


