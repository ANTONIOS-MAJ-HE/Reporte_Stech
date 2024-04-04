using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        await EnviarOrdenes();
        Console.WriteLine("Órdenes enviadas correctamente.");
    }

    static async Task EnviarOrdenes()
    {
        List<Orden> ordenes = ObtenerOrdenesDesdeBD(); // Obtener las órdenes desde la base de datos
        string jsonOrdenes = JsonConvert.SerializeObject(ordenes); // Convertir las órdenes a formato JSON

        using (HttpClient client = new HttpClient())
        {
            client.BaseAddress = new Uri("http://localhost:8000/");
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

            try
            {
                string authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyOTE0MTg2LCJpYXQiOjE3MTEzNzgxODYsImp0aSI6IjNjODMxMDM1MWFiZTRiZDA5OTIzODE4ODg4NzFjMWNjIiwidXNlcl9pZCI6MX0.3c7Hn9YZvW7GXy0CmgZyMKZWwpyypuZs773cKoLFg8s"; // Reemplazar con tu token de autenticación

                // Agregar el token de autenticación al encabezado
                client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", authToken);

                HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, "ordenes/");
                request.Content = new StringContent(jsonOrdenes, Encoding.UTF8, "application/json");

                HttpResponseMessage response = await client.SendAsync(request);

                response.EnsureSuccessStatusCode();
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"Error al enviar las órdenes: {e.Message}");
            }
        }
    }

    static List<Orden> ObtenerOrdenesDesdeBD()
    {
        List<Orden> ordenes = new List<Orden>();
        string connectionString = "Data Source= PC005;Initial Catalog= DB_ST;User Id=STEC;Password=sasa;"; // Reemplazar con tu cadena de conexión

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            string query = "SELECT CANAL AS canal, NUMERO_ORDEN AS numero_orden, NUMERO_FACTURA AS numero_factura, DNI_CLIENTE AS dni_cliente, NOMBRE_CLIENTE AS nombre_cliente, DIRECCION_CLIENTE AS direccion_cliente, REGION_VENTA AS region_venta, NOMBRE_PRODUCTO AS nombre_producto, MODELO_PRODUCTO AS modelo_producto, MARCA_PRODUCTO AS marca_producto, CATEGORIA_PRODUCTO AS categoria_producto, CODIGO_PRODUCTO_CANAL AS codigo_producto_canal, PART_NUMBER AS part_number, CANTIDAD AS cantidad, PRECIO_S_IGV AS precio_s_igv, PRECIO_C_IGV AS precio_c_igv, TOTAL_S_IGV AS total_s_igv, TOTAL_C_IGV AS total_c_igv, FECHA_ORDEN AS fecha_orden, FECHA_PROCESO AS fecha_proceso, FECHA_DESPACHO AS fecha_despacho, ST_DESPACHO AS st_despacho, ESTADO_ORDEN AS estado_orden, OBSERVACION_ORDEN AS observacion_orden FROM ST_CONS_ORDENES_NEW WHERE NUMERO_ORDEN = '32760411' ORDER BY FECHA_PROCESO DESC;"; // Reemplazar con tu consulta SQL
            SqlCommand command = new SqlCommand(query, connection);

            try
            {
                connection.Open();
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Orden orden = new Orden
                    {
                        // Asignar los valores de las columnas de la tabla a las propiedades de la clase Orden
                    canal = reader["canal"].ToString(),
                    numero_orden = reader["numero_orden"].ToString(),
                    //numero_factura = reader["numero_factura"].ToString(),
                    dni_cliente = reader["dni_cliente"].ToString(),
                    nombre_cliente = reader["nombre_cliente"].ToString(),
                    direccion_cliente = reader["direccion_cliente"].ToString(),
                    region_venta = reader["region_venta"].ToString(),
                    nombre_producto = reader["nombre_producto"].ToString(),
                    modelo_producto = reader["modelo_producto"].ToString(),
                    marca_producto = reader["marca_producto"].ToString(),
                    categoria_producto = reader["categoria_producto"].ToString(),
                    codigo_producto_canal = reader["codigo_producto_canal"].ToString(),
                    part_number = reader["part_number"].ToString(),
                    cantidad = Convert.ToInt32(reader["cantidad"]),
                    precio_s_igv = Convert.ToSingle(reader["precio_s_igv"]),
                    precio_c_igv = Convert.ToSingle(reader["precio_c_igv"]),
                    total_s_igv = Convert.ToSingle(reader["total_s_igv"]),
                    total_c_igv = Convert.ToSingle(reader["total_c_igv"]),
                    fecha_orden = Convert.ToDateTime(reader["fecha_orden"]),
                    fecha_proceso = Convert.ToDateTime(reader["fecha_proceso"]),
                    fecha_despacho = Convert.ToDateTime(reader["fecha_despacho"]),
                    st_despacho = reader["st_despacho"].ToString(),
                    estado_orden = reader["estado_orden"].ToString(),
                    //observacion_orden = reader["observacion_orden"].ToString(),
                };
                    ordenes.Add(orden);
                }
                reader.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al obtener las órdenes desde la base de datos: " + ex.Message);
            }
        }

        return ordenes;
    }
}

public class Orden
{
    public string canal { get; set; }
    public string numero_orden { get; set; }
    public string numero_factura { get; set; }
    public string dni_cliente { get; set; }
    public string nombre_cliente { get; set; }
    public string direccion_cliente { get; set; }
    public string region_venta { get; set; }
    public string nombre_producto { get; set; }
    public string modelo_producto { get; set; }
    public string marca_producto { get; set; }
    public string categoria_producto { get; set; }
    public string codigo_producto_canal { get; set; }
    public string part_number { get; set; }
    public int cantidad { get; set; }
    public float precio_s_igv { get; set; }
    public float precio_c_igv { get; set; }
    public float total_s_igv { get; set; }
    public float total_c_igv { get; set; }
    public DateTime fecha_orden { get; set; }
    public DateTime fecha_proceso { get; set; }
    public DateTime fecha_despacho { get; set; }
    public string st_despacho { get; set; }
    public string estado_orden { get; set; }
    public string observacion_orden { get; set; }
}