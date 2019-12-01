# Django-REST SubClasses of APIView

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
  
  
NOTE:- None of the classes like ListAPIView, CreateAPIView, RetrieveAPIView etc. extends APIView both are fro different packages. These are just to set some analogy.


All the operation can be performed using just 2 endpoints by these subclasses:

 1. ListCreateAPIView : don't require primary key - 127.0.0.1:8000/api
 2. RetrieveUpdateDestroyAPIView : require primary key - 127.0.0.1:8000/api/3


 Combinations -

  - ListAPIView + CreateAPIView = ListCreateAPIView
  - RetrieveAPIView + UpdateAPIView = RetrieveUpdateAPIView
  - RetrieveAPIView + DestroyAPIView = RetrieveDestroyAPIView
  - RetrieveAPIView + UpdateAPIView + DestroyAPIView = RetrieveUpdateDestroyAPIView
