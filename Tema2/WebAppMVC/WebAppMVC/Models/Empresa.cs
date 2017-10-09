using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebAppMVC.Models
{
    public class Empresa
    {
        public int Id { get; set; }

        public string Nombre { get; set; }

        public string Descripcion { get; set; }

        public string Telefono { get; set; }
    }

    public class AsociacionEmpresas
    {
        public static Empresa GetEmpresa(int i)
        {
            List<Empresa> lista = new List<Empresa>()
            {
                new Empresa
                {
                    Descripcion = "Proyectos TIC globales y servicios gestionados o en la nube: handCLOUD, handTIC, formacionTIC.",
                    Id = 1,
                    Nombre = "ALHAMBRA-EIDOS",
                    Telefono = "91 787 23 00"
                },
                new Empresa
                {
                    Descripcion = "Consultoría e ingeniería TIC, proyectos de comunicaciones y seguridad, CPDs, servicios gestionados y en cloud, soporte y mantenimiento.",
                    Id = 2,
                    Nombre = "AMBAR TELECOMUNICACIONES",
                    Telefono = "942344896"
                },
                new Empresa
                {
                    Descripcion = "Networking, Internet de las Cosas, Comunicaciones Unificadas, Infraestructuras...",
                    Id = 3,
                    Nombre = "Cisco Systems",
                    Telefono = "915907500"
                },
                new Empresa
                {
                    Descripcion = "Prestación de servicios, investigación y coordinación en materia de Ciberseguridad.",
                    Id = 4,
                    Nombre = "Instituto Nacional de Ciberseguridad (Incibe)",
                    Telefono = "91 212 76 26"
                },
            };

            return lista.FirstOrDefault(emp => emp.Id == i);
        }
    }
}