using WebAppMVC.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace WebAppMVC.Controllers
{
    public class EmpresaController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }
        public ActionResult Detalle(int Id)
        {
            Empresa model = AsociacionEmpresas.GetEmpresa(Id);
            return View(model);
        }
    }
}