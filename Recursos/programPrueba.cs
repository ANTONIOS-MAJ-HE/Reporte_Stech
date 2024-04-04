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

        Console.WriteLine("JSON de órdenes:");
        Console.WriteLine(jsonOrdenes); // Imprimir el JSON resultante

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
        string connectionString = "Data Source=LAPTOP-R1VL050P\\SQLEXPRESS2017;Initial Catalog=DB_ST;Integrated Security=True;"; // Reemplazar con tu cadena de conexión

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            string query = "SELECT CANAL, NUMERO_ORDEN FROM ST_CONS_ORDENES_NEW WHERE NUMERO_ORDEN = '32760411' ORDER BY FECHA_PROCESO DESC;"; // Reemplazar con tu consulta SQL
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
                        canal = reader["CANAL"].ToString(),
                        numero_orden = reader["NUMERO_ORDEN"].ToString(),
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
}