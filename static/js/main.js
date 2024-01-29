const listItems = document.querySelectorAll(".sidebar-list li");

listItems.forEach(item => {
     item.addEventListener("click", () => {
          let isActive = item.classList.contains("active");

          listItems.forEach(el => {
               el.classList.remove("active");
          });

          if (isActive) {
               item.classList.remove("active");
          } else {
               item.classList.add("active");
          }
     });
});


const toggleSidebar = document.querySelector(".toggle-sidebar");
const logo = document.querySelector(".logo-box");
const searchBox = document.querySelector(".search-box");
const sidebar = document.querySelector(".sidebar");

toggleSidebar.addEventListener("click", () => {
     sidebar.classList.toggle("close");
});

logo.addEventListener("click", () => {
     sidebar.classList.toggle("close");
});

searchBox.addEventListener("click", () => {
     sidebar.classList.remove("close");
});
     

// Initial call on page load
document.addEventListener('DOMContentLoaded', function () {
     updateFormILP();
});

function updateFormLP() {
     console.log('updateFormLP function is called');
     var numVariables = document.getElementById('numVariables').value;
     console.log('numVariables:', numVariables);

     var name_variable = document.getElementById('name_variable');
     name_variable.innerHTML = '<p><strong>Please give the name type of flowers</strong></p>';
     for (var j = 0; j < numVariables; j++) {
          name_variable.innerHTML += `Flower no.${j + 1} = <input type="text" name="name_variable[${j}]" required><br>`;
     }
     name_variable.innerHTML += '<br>';

}


function scrollToSection(sectionId) {
     var section = document.getElementById(sectionId);
     if (section) {
          section.scrollIntoView({ behavior: "smooth" });
     }
}

document.addEventListener('DOMContentLoaded', function () {
     document.getElementById('editProfileForm').addEventListener('submit', function (event) {
          event.preventDefault();

          if (confirm('Are you sure you want to save the changes?')) {
               document.getElementById('editProfileForm').submit();
          }
     });
});
document.addEventListener('DOMContentLoaded', function() {
     document.getElementById('changePasswordForm').addEventListener('submit', function(event) {
          event.preventDefault(); // Prevent the form from being submitted directly

          // Show a confirmation popup
          if (confirm('Are you sure you want to change your password?')) {
               // If the user confirms, submit the form
               document.getElementById('changePasswordForm').submit();
          } else {
               // If the user cancels, do nothing
          }
     });
});



