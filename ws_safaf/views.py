from django.http import HttpResponse
# import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import xmlrpc.client


class OdooHelper():   
     
    database_name = 'odoo16-saffinal'
    user = 'admin'
    password = 'admin'
    url_server = '172.16.100.59'
    
    def authenticate_odoo(self):
        # Crear una conexión al servidor Odoo
        odoo = xmlrpc.client.ServerProxy('http://'+ self.url_server + ':8069/xmlrpc/2/common')

        print(odoo.version())

        uid = odoo.authenticate(self.database_name, self.user, self.password, {})
        
        print(uid)

        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format('http://'+self.url_server +':8069'))
        return models, uid
    
    def enviar_peticion(self, models, uid, data, modelo, funcion):
        respuesta = models.execute_kw(self.database_name, uid, self.user, modelo, funcion, [data])
        return respuesta
        

# create a viewset
class EmpleadosViewSet(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='hr.employee', funcion='create_empleado')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='hr.employee', funcion='actualizar_empleado')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='hr.employee', funcion='eliminar_empleado')
        return Response(respuesta, status=status.HTTP_200_OK)
    
class CuentasViewSet(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='account.account', funcion='create_cuenta')
        
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='account.account', funcion='actualizar_cuenta')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='account.account', funcion='eliminar_cuenta')
        return Response(respuesta, status=status.HTTP_200_OK)
    

class ContactoViewSet(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo() 
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='res.partner', funcion='create_contacto')
        
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='res.partner', funcion='actualizar_contacto')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='res.partner', funcion='eliminar_contacto')
        return Response(respuesta, status=status.HTTP_200_OK)
    

class CampusViewSet(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo() 
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='saf.campus', funcion='create_campus')
        
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='saf.campus', funcion='actualizar_campus')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='saf.campus', funcion='eliminar_campus')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
class BloqueViewSet(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo() 
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='saf.bloque', funcion='create_bloques')
        
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='saf.bloque', funcion='actualizar_bloques')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='saf.bloque', funcion='eliminar_bloques')
        return Response(respuesta, status=status.HTTP_200_OK)
    

class EspacioFisicoViewSet(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info_create = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo() 
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_create, 
                                   modelo='saf.espacio_fisico', funcion='create_espacios_fisicos')
        
        return Response(respuesta, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        info_update = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_update, 
                                   modelo='saf.espacio_fisico', funcion='actualizar_espacios_fisicos')
        return Response(respuesta, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        info_delete = request.data 
        odoo_helper = OdooHelper()
        models, uid = odoo_helper.authenticate_odoo()  
        respuesta = odoo_helper.enviar_peticion( models=models, uid=uid, data=info_delete, 
                                   modelo='saf.espacio_fisico', funcion='eliminar_espacios_fisicos')
        return Response(respuesta, status=status.HTTP_200_OK)
        
