# NLK Digital Library Books Catalog

A catalog of the books that the [Wikimedia Commons Library back up project](https://commons.wikimedia.org/wiki/Commons:Library_back_up_project/file_list/Books_in_the_Digital_Library_of_the_National_Library_of_Korea/books) copied from the Digital Library of the National Library of Korea (국립중앙도서관 디지털도서관).

위키미디어 공용 백업 프로젝트가 국립중앙도서관 디지털도서관에서 옮겨 온 도서 목록(하위 페이지 `books/1`–`books/97`)을 정리한 엑셀 파일입니다.

## 파일

`NLK_books_catalog.xlsx`

| 시트 | 내용 |
|---|---|
| 설명 | 자료 출처와 작업 방법 |
| 전체목록 | 73,286건. ID, 원제목, 한국어 제목, 저자, 발행연도, 시대, 분류, 한 줄 요약, 발행처, 파일 수, 링크 |
| 시대×분류 | 시대와 분류의 교차 집계 |
| 분류별 | 분류마다 책 수와 대표 도서 |
| 고문서유형 | 간찰·제문·교지 등 낱장 문서의 유형별 개수 |

## 작업 방법

- **시대:** 발행연도 필드를 스크립트로 서기로 바꿔 나눴습니다. 서기 연도, 조선 왕의 재위년, 일본·대한제국·중국 연호를 처리합니다. 연도가 없는 책은 제목과 저자로 시대를 추정했고 '추정'으로 표시했습니다.
- **한국어 제목·분류·한 줄 요약:** 제목, 저자, 발행 정보를 바탕으로 AI(Claude)가 작성했습니다.

## 주의

- 원문 PDF를 읽고 쓴 요약이 아닙니다. 잘 알려지지 않은 책은 요약이 일반적이거나 틀릴 수 있습니다.
- 간찰, 교지, 영수증 같은 낱장 고문서 12,846건은 번역하지 않고 유형만 집계했습니다.
- 제목이 같은 여러 권은 같은 번역과 요약을 함께 씁니다.

서지 원자료는 국립중앙도서관과 위키미디어 공용에서 가져왔습니다.
