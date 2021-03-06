# Part 1. 코딩 인터뷰

## 1장 - 코딩 인터뷰

- 코딩 인터뷰: 기술 직군 채용을 위한 기술 문제 중심의 개발 인터뷰
- 코딩 인터뷰 (코딩 면접)
  - 오프라인; 온사이트 코딩 인터뷰 / 오프라인 코딩 인터뷰
    - 화이트 보드 코딩 인터뷰
  - 온라인 코딩 인터뷰
- 코딩 테스트 (코딩 시험)
  - 온라인 코딩 테스트

### 코딩 인터뷰를 위한 온라인 테스트 플랫폼

- 해커랭크
  - 테스트 케이스 보여주지 않음 (기업 재량)
  - 일부 테스트 틀리거나 타임아웃 시 코드를 보며 스스로 문제 찾아내야 함
  - 스스로 코드 디버깅을 통해 문제를 풀어내는 역량 필요
- 코딜리티
- 리모트 인터뷰
  - 단 하나의 입력값만 통과하면 문제 풀이된 것으로 간주
  - 내부적으로 별도로채점하여 기업 담당자에게 점수 알려줌
  - 시험 치른 사람은 내 코드가 정답인지, 몇 점인지 전혀 알 수 없음
  - 가장 까다롭게 평가 받는 방식
  - 디버깅 필요조차 모르게 될 수 있음
- 프로그래머스 (국내)
- 개인용 문제 풀이 서비스
  - 리트코드
  - 백준 (국내)

### 국내 기업의 코딩 테스트 플랫폼 활용 현황

- 카카오 모든 개발 직군 채용 시 코딩 테스트 의무화
- 프로그래머스, 해커랭크, 코딜리티
- 삼성전자는 별도 환경에 별도 자체 플랫폼 사용 (오프라인)

### 온라인 코딩 테스트의 사전 준비사항

- 연습장과 필기 도구
  - 값의 변화나 최종 결과를 기록하고 머릿속에 떠올린 구조와 비교하면서 풀이
- 프로그래밍 언어
  - 파이썬
- 나만의 코드 스니펫
  - ex) 연결 리스트 뒤집거나 삭제 등 작업 (헷갈릴 수 있는 것)
  - 로컬 컴퓨터에 별도 저장
  - 깃허브 Gist 이용 가능
  - 스스로 많이 연습하고 풀어보면서 <br/>
    자신에게 가장 어려운 알고리즘이나 코드 위주로 직접 정리
    권장
- 모든 테스트 케이스 통과하도록 풀기
  - 최적화 신경 쓰기
- 타임 아웃 발생 경우
  - 같은 알고리즘이어도 언어별로 편차 발생 가능
  - 파이썬은 다른 언어에 비해 알고리즘 최적화 고민 많이 필요
- 예외 처리 필수
  - 입력값에 대한 검증 (null, 0, 입력값 없음)
- 잘못 접근 풀이 대처
  - 문제당 제한 시간 설정 후 시간 초과시 바로 다음 문제로 넘어가기
- 풀이 시간 초과시 포기?
  - 시간이 조금 더 주어지면 다 풀 수 있고 면접관의 이메일 주소 알 때 <br/>
    => 시간 초과 이후에도 계속 풀이 시도, 면접관에게 이메일 보내기
- 코딩 도구 필요성
  - VS Code
  - PyCharm 커뮤니티 에디션
- IDE
  - IDE 없어도 개발이 가능하다는 점을 면접관에게 분명하게 강조
  - 개발을 못해서 IDE를 택한 것이 아니라 개발의 편의성을 위해 택한 것을 강조
- REPL 도구로 코드 검증
  - 즉시 실행하여 모호한 알고리즘 바로 검증 가능 (디버깅)

### 화이트보드 코딩 인터뷰

- 핵심을 관통하는 알고리즘 중심으로 구현

### [Note]

- 테스트 케이스: 특정한 테스트 목표를 달성하기 위해 <br/>
  실행되는 입력, 실행 조건, 테스트 절차, 기대 결과 등의 스펙
- TDD (테스트 주도 개발): 가급적 테스트를 많이 진행하여 일부러 버그를 유발해서 <br/>
  문제를 수정해 나아가는 형태로 개발 진행
- REPL (Read-Eval-Print-Loop): 사용자 입력에 대한 실행 결과 바로 되돌려 주는 상호작용 환경
  - ex) 주피터 노트북
