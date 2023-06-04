CREATE TABLE activity_logs (
  id integer primary key autoincrement, /* 로그 아이디 */
  datetime text, /* 발생 시각 */
  eventType number, /* EventType 타입 Enum */
  relates text, /* 사용자 식별자 */
  summary text, /* 요약 */
  detail text /* 상세 */
);

CREATE TABLE users ( /* with organization */
  id text not null,
  name text not null,
  acl number not null,
  user_type number not null,
  image_path text not null
);

CREATE TABLE organization (
  /*
    일반 사용자와 조직 모두 users 테이블에 일괄 관리되고 있음: user_type 플래그로 조직 여부 판단
    사용자 - 조직 매치 테이블
  */
  user_id text not null, 
  org_user_id text not null
);
/* 
  PersonData 객체 설계 중 organization을 객체당 하나만 받도록 작성하여
  organization이 유저 당 하나만 사용되도록 코드가 작성되고 있음
  TODO: 유저 당 여러 개 organization도 지원하도록 수정 필요
*/

CREATE TABLE pass_reserved (
  event_id text not null,
  passer text not null,
  related text not null,
  timeat number not null,
  description text not null
);

CREATE TABLE person_list_facenet (
  /*
    개별 얼굴 인식 쿼리 사건 목록: 인덱스
  */
  id text not null,
  invoked number not null /* 쿼리가 발생된 시각의 UNIX Timestamp: 최근 순 정렬에 사용 */
);

CREATE TABLE person_list_facenet_each_person (
  /*
    개별 얼굴 인식 쿼리의 결과
  */
  id text not null, /* 쿼리에서 검출된 인원의 user id*/
  event_id text not null, /* 얼굴 인식 쿼리 사건의 id(person_list_facenet.id) */
  probability number not null, /* 정확도 */
  description text not null /* 사용자에 의해 추가되는 부가 설명 */
);
