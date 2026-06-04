fetch("http://localhost:5000/api/users")
  .then(response => response.json())
  .then(users => {

    const table = document.getElementById("usersTable");

    users.forEach(user => {

      const row = `
        <tr>
          <td>${user.id}</td>
          <td>${user.name}</td>
          <td>${user.email}</td>
        </tr>
      `;

      table.innerHTML += row;
    });

  })
  .catch(error => console.log(error));