# Django-REST_SubClass_of_APIView

All the CRUD operation using the subclasses of APIVIew

APIView
  - ListAPIView
  - CreateAPIView

  - RetrieveAPIView
  - UpdateAPIView
  - DestroyAPIView

  - ListCreateAPIView
  - RetrieveUpdateAPIView
  - RetrieveDestroyAPIView

  - RetrieveUpdateDestroyAPIView


All the operation can be performed using just 2 endpoints by these subclasses -
 - ListCreateAPIView : don't require primary key - 127.0.0.1:8000/api
 - RetrieveUpdateDestroyAPIView : require primary key - 127.0.0.1:8000/api/3


 Combinations -

  - ListAPIView + CreateAPIView = ListCreateAPIView
  - RetrieveAPIView + UpdateAPIView = RetrieveUpdateAPIView
  - RetrieveAPIView + DestroyAPIView = RetrieveDestroyAPIView
  - RetrieveAPIView + UpdateAPIView + DestroyAPIView = RetrieveUpdateDestroyAPIView
