import { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'
import Button from './Buttons'

const Header = () => {
  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext)
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    setIsLoggedIn(false)
    navigate('/login')
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
      <div className="container py-2">
        
        {/* Logo / Brand */}
        <Link className="navbar-brand fw-bold fs-4 text-info" to="/">
          Stock Prediction Portal Application 
        </Link>

        {/* Right side */}
        <div className="d-flex align-items-center gap-2">
          {isLoggedIn ? (
            <>
              <Button
                text="Dashboard"
                class="btn-outline-info"
                url="/dashboard"
              />
              <button
                className="btn btn-outline-danger"
                onClick={handleLogout}
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Button
                text="Login"
                class="btn-outline-info"
                url="/login"
              />
              <Button
                text="Register"
                class="btn-info"
                url="/register"
              />
            </>
          )}
        </div>

      </div>
    </nav>
  )
}

export default Header