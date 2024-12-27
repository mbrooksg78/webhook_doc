=======================
Especificación Técnica
=======================

Endpoint
========

.. code-block:: none

   URL: https://<servidor>:<puerto>/sire/confirmation
   Método: POST
   Formato: JSON

.. important::
   Todos los endpoints requieren autenticación mediante token JWT y firma HMAC.

.. list-table:: Cabeceras HTTP
    :widths: 25 75
    :header-rows: 1

    * - Nombre
      - Descripción
    * - X-Odoo-Signature
      - Firma HMAC-SHA256 del cuerpo de la solicitud
    * - Authorization
      - Bearer Token JWT proporcionado por Odoo
    * - Content-Type
      - "application/json"

.. note::
    La firma se genera utilizando el token de autenticación como clave secreta

|
|

Estructura de la Solicitud
---------------------------
.. code-block:: json

   {
       "move_ref": "<string>",
       "status": "<string>",
       "timestamp": "<string>",
       "details": {
           "user_id": "<string>",
           "comments": "<string>"
       }
   }


Respuestas
----------
Respuesta Exitosa (200 OK)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: json

   {
       "status": "success",
       "message": "Requerimiento procesado correctamente",
       "data": {
           "move_ref": "<string>",
           "processed_at": "<timestamp>"
       }
   }

Respuestas de Error
^^^^^^^^^^^^^^^^^^^

401 Unauthorized
~~~~~~~~~~~~~~~~~~
.. code-block:: json

   {
       "error": "Error de autenticación",
       "details": "Token inválido o expirado"
   }

404 Not Found
~~~~~~~~~~~~~~~
.. code-block:: json

   {
       "error": "Requerimiento no encontrado",
       "details": "El ID de requerimiento especificado no existe"
   }

500 Internal Server Error
~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: json

   {
       "error": "Requerimiento procesado",
       "details": "El requerimiento ya h sido procesado"
   }
