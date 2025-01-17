from bd import obtener_conexion

def insertar(estado, introduccion, infraFisica, infraTecnologica, organigrama, descAreaRelaciones, descLabores, conclusiones, recomendaciones, bibliografia, giroEmpresa, representanteLegal, cantTrabajadores, vision, mision, urlAnexo, idPractica):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO INFORME_FINAL_ESTUDIANTE(fechaEntrega, estado, introduccion, infraFisica, infraTecnologica, organigrama, descAreaRelaciones, descLabores, conclusiones, recomendaciones, bibliografia, giroEmpresa, representanteLegal, cantTrabajadores, vision, mision, urlAnexo, idPractica) VALUES (now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (estado, introduccion, infraFisica, infraTecnologica, organigrama, descAreaRelaciones, descLabores, conclusiones, recomendaciones, bibliografia, giroEmpresa, representanteLegal, cantTrabajadores, vision, mision, urlAnexo, idPractica))
    conexion.commit()
    conexion.close()

def buscar_id(idInformeFinalEst):
    conexion = obtener_conexion()
    informe = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT concat(e.nombres, ' ', e.apellidos) as estudiante, em.razonSocial, em.direccion, i.* FROM INFORME_FINAL_ESTUDIANTE i inner join PRACTICA p on p.idPractica = i.idInformeFinalEst inner join ESTUDIANTE e on e.idEstudiante = p.idEstudiante inner join JEFE_INMEDIATO ji on ji.idJefe = p.idJefe inner join EMPRESA em on em.idEmpresa = ji.idEmpresa WHERE idInformeFinalEst = %s", (idInformeFinalEst,))
        informe = cursor.fetchone()
    conexion.close()
    return informe

def actualizar(estado, introduccion, infraFisica, infraTecnologica, organigrama, descAreaRelaciones, descLabores, conclusiones, recomendaciones, bibliografia, giroEmpresa, representanteLegal, cantTrabajadores, vision, mision, urlAnexo, idPractica, idInformeFinalEst):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE INFORME_FINAL_ESTUDIANTE SET fechaEntrega = now(), estado = %s, introduccion = %s, infraFisica = %s, infraTecnologica = %s, organigrama = %s, descAreaRelaciones = %s, descLabores = %s, conclusiones = %s, recomendaciones = %s, bibliografia = %s, giroEmpresa = %s, representanteLegal = %s, cantTrabajadores = %s, vision = %s, mision = %s, urlAnexo = %s WHERE idPractica = %s and idInformeFinalEst = %s",
                       (estado, introduccion, infraFisica, infraTecnologica, organigrama, descAreaRelaciones, descLabores, conclusiones, recomendaciones, bibliografia, giroEmpresa, representanteLegal, cantTrabajadores, vision, mision, urlAnexo, idPractica, idInformeFinalEst))
    conexion.commit()
    conexion.close()

def observar_informe(observacion, idPractica, idInformeFinalEst):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE INFORME_FINAL_ESTUDIANTE SET estado='O', set observacion = %s WHERE idPractica = %s and idInformeFinalEst = %s",
                       (observacion, idPractica, idInformeFinalEst))
    conexion.commit()
    conexion.close()

def aceptar_informe(idPractica, idInformeFinalEst):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE INFORME_FINAL_ESTUDIANTE SET estado='A', set observacion = '' WHERE idPractica = %s and idInformeFinalEst = %s",
                       (idPractica, idInformeFinalEst))
    conexion.commit()
    conexion.close()